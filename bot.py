from argparse import ArgumentParser
import logging
import telepot
import time
import os

from flask import Flask, request
from regexes_intent_classifier import regex_intent_classifier

from answer_with_bert import get_bert_model
from dm_baseline import dialogue_manager
from fms import ConversationFMS
from logger_setup import set_logger
from nlu import get_intent, get_model
from state import State
from story import get_story_graph
from telegram_bot.credentials import BOT_TOKEN


bot = telepot.Bot(BOT_TOKEN)
bot.setWebhook("https://1cab4515fc9c.ngrok.io/chat")

app = Flask(__name__)

BOT_NAME = "storyteller"

logger = logging.getLogger(__name__)
set_logger("INFO", "./logs/storyteller-baseline.log")

parser = ArgumentParser()
parser.add_argument('-p', "--port", type=int, default=5130)
parser.add_argument('-l', '--logfile', type=str, default='logs/' + BOT_NAME + '.log')
parser.add_argument('-cv', '--console-verbosity', default='info', help='Console logging verbosity')
parser.add_argument('-fv', '--file-verbosity', default='info', help='File logging verbosity')

state_object = None
story_fsm = None
chat_ids = [1334492905, 1030004241]
interpreter = get_model()
bert_model = get_bert_model()


@app.route('/chat', methods=["POST"])
def telegram_webhook():
    # retrieve the message in JSON and then transform it to Telegram object
    global state_object
    global story_fsm
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        if chat_id in chat_ids:
            bot.sendMessage(chat_id, "This session is now expired. Thanks for your collaboration.")
        else:
            bot.sendChatAction(chat_id, action="typing")
            print("chat_id:", chat_id)
            if "text" in update["message"]:
                text = update["message"]["text"]
                print("received", text)
                if text == '/start':
                    # print the welcoming message
                    user_utterance = text
                    story_graph = get_story_graph()
                    visited_nodes = []
                    intent = ""
                    previous_intent = ""
                    state_object = State(story_graph, visited_nodes, user_utterance, intent, bert_model, previous_intent)
                    bot.sendMessage(chat_id, "Starting storyteller bot... Done.")
                    story_fsm = ConversationFMS("introduction")
                else:
                    user_utterance = text
                    if state_object is None:
                        # need to create the story graph
                        story_graph = get_story_graph()
                        visited_nodes = []
                        intent = ""
                        previous_intent = ""
                        state_object = State(story_graph, visited_nodes, user_utterance, intent, bert_model, previous_intent)
                    else:
                        state_object.utterance = user_utterance
                        state_object.previous_intent = state_object.intent
                        state_object.intent = ""

                    # --------------------- NATURAL LANGUAGE UNDERSTANDING  --------------------- #
                    # We try to use regex and if else statement to catch the intent before using rasa
                    regex_intent_classifier(user_utterance, state_object)
                    if state_object.intent == "":
                        nlu_result = get_intent(interpreter, user_utterance)
                        state_object.intent = nlu_result["intent"]["name"]
                    # initialise fsm
                    if story_fsm is None:
                        story_fsm = ConversationFMS("introduction")
                    # set new state
                    state_object.set_new_state(story_fsm)
                    # -------------------- DIALOGUE MANAGER ------------------ #
                    answer = dialogue_manager(state_object, story_fsm)

                    logger.info("------- Turn info ----------")
                    logger.info("User utterance: {}".format(user_utterance))
                    logger.info("User intent: {}".format(state_object.intent))
                    logger.info("Bot state: {}".format(story_fsm.state))
                    logger.info("Bot answer: {}".format(answer))
                    logger.info("---------------------------")
                    # ---------------------------------------------------------- #
                    time.sleep(2)
                    bot.sendMessage(chat_id, answer)
    return 'ok'


if __name__ == "__main__":
    args = parser.parse_args()

    if not os.path.exists("logs/"):
        os.makedirs("logs/")

    app.run(host="0.0.0.0", port=args.port)