import random
import time

from rasa.nlu.model import Interpreter

def get_model():
    model = "/home/sabrina/PycharmProjects/storyteller_DS/rasa_folder/models/nlu"

    interpreter = Interpreter.load(model)
    return interpreter


def get_intent(interpreter, utterance):
    """
    retrieves intent from user utterance
    :param utterance: String - user utterance
    :return: string - intent
    """
    interpretation = interpreter.parse(utterance)
    return interpretation


if __name__ == "__main__":
    listener_affirm = ["I agree", "yes they sure can", "Yea", "Ok", "oh right",
                  "ah okay", "yes thanks", "yes please"]
    listener_ask_for_story = ["Tell me your story", "you are a good storyteller have you any others?",
                              "do you have a story?", "another story?", "Have you got any more stories to tell me?",
                              "another one?", "do you have a story to tell?", "what is your story?"]
    listener_greet = ["Hi", "hello", "Hello", "hey", "Hey", "hi!!", "hello", "good morning"]
    listener_thanks = ["ok nice, thanks for the story", "Thanks!", "Alright! Thank you for telling them to me.", "Ok thanks",
                       "thank you for the story, it was interesting", "thanks", "thanks!!", "thanks for the story"]
    listener_comment = ["So I have heard even though a mouse isnt much of a meal", "Sometimes dads give that impression",
                        "It's a good thing the lion let the mouse go then or he would still be in the net",
                        "Have a most wonderful rest of your vacation.", "They must not have had much to sell",
                        "Tuna are really large fish so i can see why they would need a cart to move them around",
                        "Vacations are never long enough. What types of fish did you see.",
                        "And then he begged for his life", "Bet you had a great time"]
    listener_exclaim_pos = ["That is really cool!", "wow!", "wow thats really early", "sounds interesting",
                            "oh nice", "That’s good", "That is good", "It sounds like you had a great time."]
    listener_exclaim_neg = ["oh thats sad", "That’s not good", "That is terrible", "that is a shame/", "How sad",
                            "Oh, that's a shame.", "awful", "Very greedy"]
    listener_request_increment = ["Tell me", "Yea go on", "go on", "Alright, thank you. Please continue.",
                                  "What happens next", "and?", "and then?", "go on"]
    listener_ynq = ["So was this a type of excursion you went on?", "See any pearls in it? ",
                    "Did you do the scuba diving there?", "Was is made of gold?", "Was there anything else? ",
                    "Were you there on vacation?", "So they killed the goose?", "Was is made of gold?"]
    listener_whq = ["What does the mouse do", "Why is it sad",
                    "What did you see while doing it?", "How did the lion respond?", "Where did you go?",
                    "How many days did they get a golden egg?", "Terrified of what ?", "What you need a camera?"]
    listener_goodbye = ["ok bye", "goodbye", "bye bye", "it was nice, bye!", "ok see you bye", "see you", "see ya",
                        "Goodbye!"]

    interpreter = get_model()

    print("Affirm: ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_affirm[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("Ask_for_Story: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_ask_for_story[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("Greet: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_greet[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("Thanks: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_thanks[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("Comment: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_comment[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("Exclaim Pos: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_exclaim_pos[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("Exclaim Neg: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_exclaim_neg[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("Request increment: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_request_increment[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("YNQ: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_ynq[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("WHQ: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_whq[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")
    print(" ")
    print("Goodbye: ")
    print(" ")
    for i in range(8):
        nluResult = get_intent(interpreter, listener_goodbye[i])
        intent = nluResult["intent"]["name"]
        print(intent)
    print(" ------------------------ ")


