import random
import sys
import logging


logger = logging.getLogger(__name__)

_recsys_templates = [
    "....I think you should do {}.",
    ".......{}"
]


# Intent: User preference: -ive
# Example: (I dont like {})
_questionaire = [
    "Welcome back {}. So, what would you like to do?"
]


# Intent: User preference: +ive / Linked Concepts
# Example: (I like {})
_driver_templates = {
    "x_intent": {
        # prop - artist
        # entity - band
        # linked entity - another artist
        "a_entity": [
            "Okay. I guess you know that {entity} is in {quest}. What is {object} that you like to find?"
        ]
    }
}


class NLG:
    def fill_template(self, state_dic):
        pass

    def fill_explanations(self, state_dic):
        pass

    def fill_recommendation(self, state_dic):
        pass

    def fill_questionaire(self, state_dic):
        pass


class StorytellerGenerator(NLG):
    def __init__(self, args):
        logger.info("Creating features from dataset file at %s", args.out_dir)

    def fill_template(self, state_dic):
        templates = _driver_templates
        template_fillers = {k: v["label"] for k, v in results.items() if type(v) == dict}
        ## here template_fillers should have "entity", "quest", "object"
        # whatever required by your fillers

        if "x_intent" in results["intents"]:
            curr_templates = templates["x_intent"]
            template = random.choice(curr_templates["a_entity"])
            return template.format(**template_fillers)
        else:
            logger.info("Cant generated template for: {}".format(results))

    def fill_recommendation(self, state_dic):
        template = random.choice(_recsys_templates)
        game_play = state_dic["game_play"]

        return template.format(game_play)

    def fill_questionaire(self, state_dic):
        # if dic; use this:
        # template = questionaire[state_dic["ref_key"]]
        # if list; use this:
        template = random.choice(_questionaire)
        return template.format(state_dic["entity"])


if __name__ == "__main__":
    results = {
               "intent": {},
               "entity": {},
               "quest": {}
               }
    drivers = StorytellerGenerator()
    print(drivers.fill_template(results))
    # print(drivers.fill_explanations(results))
