import random
import sys
import logging

logger = logging.getLogger(__name__)

# --------------- FILL THESE DICTIONARIES WITH TEMPLATES ---------------------- #
# Intent: User preference: +ive / Linked Concepts
# Example: (I like {})


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
    "ynq": ["Not sure, we'll see."],
    "whq": ["Not sure, we'll see."],
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
    "greet": [],
    "goodbye": [],
    "affirm": [],
    "deny": [],
    "exclaim_neg": [],
    "exclaim_pos": [],
    "thanks": [],
    "ynq": [],
    "whq": [],
    "idk_response": [],
    "request_increment": [],
    "refocus_topic": [],
    "clarification_request": [],
    "correction": [],
    "ask_if_ended": [],
    "ask_for_story": [],
    "comment": [],
    "feedback_prompt": [],
}

_closing_templates = {
    "greet": [],
    "goodbye": [],
    "affirm": [],
    "deny": [],
    "exclaim_neg": [],
    "exclaim_pos": [],
    "thanks": [],
    "ynq": [],
    "whq": [],
    "idk_response": [],
    "request_increment": [],
    "refocus_topic": [],
    "clarification_request": [],
    "correction": [],
    "ask_if_ended": [],
    "ask_for_story": [],
    "comment": [],
    "feedback_prompt": [],
}

_answering_templates = {
    "greet": [],
    "goodbye": [],
    "affirm": [],
    "deny": [],
    "exclaim_neg": [],
    "exclaim_pos": [],
    "thanks": [],
    "ynq": [],
    "whq": [],
    "idk_response": [],
    "request_increment": [],
    "refocus_topic": [],
    "clarification_request": [],
    "correction": [],
    "ask_if_ended": [],
    "ask_for_story": [],
    "comment": [],
    "feedback_prompt": [],
}

_answering_f_templates = {
    "greet": [],
    "goodbye": [],
    "affirm": [],
    "deny": [],
    "exclaim_neg": [],
    "exclaim_pos": [],
    "thanks": [],
    "ynq": [],
    "whq": [],
    "idk_response": [],
    "request_increment": [],
    "refocus_topic": [],
    "clarification_request": [],
    "correction": [],
    "ask_if_ended": [],
    "ask_for_story": [],
    "comment": [],
    "feedback_prompt": [],
}

_ans_bidaf_templates = {
    "greet": [],
    "goodbye": [],
    "affirm": [],
    "deny": [],
    "exclaim_neg": [],
    "exclaim_pos": [],
    "thanks": [],
    "ynq": [],
    "whq": [],
    "idk_response": [],
    "request_increment": [],
    "refocus_topic": [],
    "clarification_request": [],
    "correction": [],
    "ask_if_ended": [],
    "ask_for_story": [],
    "comment": [],
    "feedback_prompt": [],
}

_link_to_survey_templates = {
    "greet": [],
    "goodbye": [],
    "affirm": [],
    "deny": [],
    "exclaim_neg": [],
    "exclaim_pos": [],
    "thanks": [],
    "ynq": [],
    "whq": [],
    "idk_response": [],
    "request_increment": [],
    "refocus_topic": [],
    "clarification_request": [],
    "correction": [],
    "ask_if_ended": [],
    "ask_for_story": [],
    "comment": [],
    "feedback_prompt": [],
}


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

    # def fill_template(self, state_dic):
    #     templates = _driver_templates
    #     template_fillers = {k: v["label"] for k, v in results.items() if type(v) == dict}
    #     ## here template_fillers should have "entity", "quest", "object"
    #     # whatever required by your fillers
    #
    #     if "greet" in results["intents"] and "introduction" in results["state"]:
    #         curr_templates = templates["greet"]
    #         template = random.choice(curr_templates["introduction"])
    #         return template.format(**template_fillers)

    def fill_intro(self, state_dic):
        templates = _intro_templates
        template_fillers = {'text': state_dic["text"]}

        if "greet" in state_dic["intents"]:
            curr_templates = templates["greet"]
            template = random.choice(curr_templates)
            return template
        elif "request_increment" in state_dic["intents"]:
            curr_templates = templates["request_increment"]
            template = random.choice(curr_templates)
            return template.format(**template_fillers)
        else:
            logger.info("Cant generated template for: {}".format(state_dic))

    def fill_storytelling(self, state_dic):
        templates = _storytelling_templates
        if "greet" in state_dic["intents"]:
            curr_templates = templates["greet"]
            template = random.choice(curr_templates)
            return template
        else:
            logger.info("Cant generated template for: {}".format(state_dic))

    def fill_closing(self, state_dic):
        templates = _closing_templates
        if "greet" in state_dic["intents"]:
            curr_templates = templates["greet"]
            template = random.choice(curr_templates)
            return template
        else:
            logger.info("Cant generated template for: {}".format(state_dic))

    def fill_answering(self, state_dic):
        templates = _answering_templates
        if "greet" in state_dic["intents"]:
            curr_templates = templates["greet"]
            template = random.choice(curr_templates)
            return template
        else:
            logger.info("Cant generated template for: {}".format(state_dic))

    def fill_answering_f(self, state_dic):
        templates = _answering_f_templates
        if "greet" in state_dic["intents"]:
            curr_templates = templates["greet"]
            template = random.choice(curr_templates)
            return template
        else:
            logger.info("Cant generated template for: {}".format(state_dic))

    def fill_ans_bidaf(self, state_dic):
        templates = _ans_bidaf_templates
        if "greet" in state_dic["intents"]:
            curr_templates = templates["greet"]
            template = random.choice(curr_templates)
            return template
        else:
            logger.info("Cant generated template for: {}".format(state_dic))

    def fill_link_to_survey(self, state_dic):
        templates = _link_to_survey_templates
        if "greet" in state_dic["intents"]:
            curr_templates = templates["greet"]
            template = random.choice(curr_templates)
            return template
        else:
            logger.info("Cant generated template for: {}".format(state_dic))



# if __name__ == "__main__":
#     results = {
#         "intent": {},
#         "entity": {},
#         "pointer_story": {},
#         "text": {}
#     }
#     drivers = StorytellerGenerator()
#     print(drivers.fill_template(results))
