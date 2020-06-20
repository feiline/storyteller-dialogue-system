import random
import sys
import logging

logger = logging.getLogger(__name__)


_intro_templates = {
    "greet": [
        "Hello! I have a story to tell you",
        "Hello, are you here for a story?",
        "Hi, would you like to hear a story?",
    ],
    "goodbye": ["Would you like to hear a story?"],
    "affirm": [ "Ok, here is the story: {text} "],
    "deny": [  # TODO: write something that makes sense
        "You can close this session if you wish. Write 'stop' to exit or ' "],
    "exclaim_neg": [   # TODO: write something that makes sense
         "You can close this session if you wish. Write 'stop' to exit or ' "],
    "exclaim_pos": ["Ok, here is the story: {text}"],
    "thanks": ["Ok, here is the story: {text}"],
    "idk_response": ["Well, just in case, here is the story: {text}"],
    "request_increment": ["{text}"],
    "refocus_topic": ["I will tell you a story that I know. Shall I start?"],
    "clarification_request": ["I will tell you a story that I know. Shall I start?"],
    "correction": ["I will tell you a story that I know. Shall I start?"],
    "ask_if_ended": ["It is not started yet. Shall I start?"],
    "ask_for_story": ["{text}"],
    "comment": ["Ok, here is the story: {text}"],
    "feedback_prompt": [
        "Yes, sorry. are you here for a story?"
        "I'm here. Would you like to hear a story?"
    ]
}

_storytelling_templates = {
    "greet": ["{text}"],
    "goodbye": ["{text}"],
    "affirm": ["{text}"],
    "deny": ["{text}"],
    "exclaim_neg": ["{text}"],
    "exclaim_pos": ["{text}"],
    "thanks": ["{text}"],
    "ynq": ["{text}"],
    "whq": ["{text}"],
    "request_increment": ["{text}"],
    "clarification_request": ["{text}"],
    "ask_if_ended": ["{text}"],
    "ask_for_story": ["{text}"],
    "comment": ["{text}"],
    "feedback_prompt": ["{text}"],
}

_closing_templates = {}

_answering_templates = {}

_answering_f_templates = {}

_ans_bidaf_templates = {}

_link_to_survey_templates = {}


class NLG:
    def fill_intro(self, state_dic):
        pass

    def fill_storytelling(self, state_dic):
        pass

    def fill_closing(self, state_dic):
        pass

    def fill_answering(self, state_dic):
        pass

    def fill_answering_f(self, state_dic):
        pass

    def fill_ans_bidaf(self,state_dic):
        pass

    def fill_link_to_survey(self, state_dic):
        pass


class StorytellerGenerator(NLG):
    def __init__(self, args):
        logger.info("Creating features from dataset file at ")

    def fill_intro(self, state_dic):
        templates = _intro_templates
        template_fillers = {'text': state_dic["text"]}
        no_story = ["greet", "goodbye", "ynq", "whq", "clarification_request",
                    "ask_if_ended", "feedback_prompt"]
        with_story = ["affirm", "exclaim_neg", "exclaim_pos", "thanks", "request_increment",
                      "ask_for_story", "comment"]
        for intent in no_story:
            if intent in state_dic["intents"]:
                curr_templates = templates[intent]
                template = random.choice(curr_templates)
                return template
        for intent2 in with_story:
            if intent2 in state_dic["intents"]:
                curr_templates = templates[intent2]
                template = random.choice(curr_templates)
                return template.format(**template_fillers)

    def fill_storytelling(self, state_dic):
        templates = _storytelling_templates
        template_fillers = {'text': state_dic["text"]}
        with_story = ["affirm", "exclaim_neg", "exclaim_pos", "thanks", "request_increment",
                      "ask_for_story", "comment"]
        no_story = ["greet", "goodbye", "ynq", "whq", "clarification_request",
                    "ask_if_ended", "feedback_prompt"]
        for intent in with_story:
            if intent in state_dic["intents"]:
                curr_templates = templates["greet"]
                template = random.choice(curr_templates)
                return template.format(**template_fillers)
        for intent in no_story:
            if intent in state_dic["intents"]:
                curr_templates = templates[intent]
                template = random.choice(curr_templates)
                return template.format(**template_fillers)
        # else:
        #     logger.info("Cant generated template for: {}".format(state_dic))

    def fill_closing(self, state_dic):
        templates = _closing_templates

    def fill_answering(self, state_dic):
        templates = _answering_templates

    def fill_answering_f(self, state_dic):
        templates = _answering_f_templates

    def fill_ans_bidaf(self, state_dic):
        templates = _ans_bidaf_templates

    def fill_link_to_survey(self, state_dic):
        templates = _link_to_survey_templates


# if __name__ == "__main__":
#     results = {
#         "intent": {},
#         "entity": {},
#         "pointer_story": {},
#         "text": {}
#     }
#     drivers = StorytellerGenerator()
#     print(drivers.fill_template(results))
