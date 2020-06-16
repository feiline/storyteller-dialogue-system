# Determina cosa accade in ogni stato.
# Può essere scritto come un univo metodo chiamato da bot.py
# STAI USANDO LA MACCHINA A STATI FINITI
from nlg import StorytellerGenerator, NLG
from story import DICT_STORY


def introduction(results):
    """
    Where to find information if state is Introduction
    :param results: dictionary with info
    :return: string - text
    """
    drivers = StorytellerGenerator(NLG)
    results['text'] = DICT_STORY['1']
    return drivers.fill_intro(results)

#
# def storytelling(results):
#     # TODO check the story is not finished. If finished, that closing
#     temp = 1
#     if temp != 1:
#         # TODO nlg template story is fished
#         fsm.story_ends()
#         return "template"
#     else:
#         if intent == "greet" or intent == "affirm" or intent == "deny" or intent == "thanks"\
#                 or intent == "request_increment" or intent == "comment":
#             # TODO: return next piece of information
#             return 1
#         elif intent == "goodbye":
#             # TODO: chiedi se l'utente se ne vuole andare o se continui?
#             return 1
#         elif intent == "exclaim_neg" or intent == "exclaim_pos":
#             # TODO: "IKR?" nlp template + next bit of the story
#             return 1
#         elif intent == "ynq" or intent == "whq":
#             # TODO: call bidaf
#             fsm.question()
#             return 1
#         elif intent == "refocus_topic" or intent == "clarification_request":
#             # TODO: return la frase precedente in template nlg
#             return 1
#         elif intent == "ask_if_ended":
#             # TODO: if story ended say yes, if not say no. Add checking to the story
#             return 1
#         elif intent == "ask_for_story":
#             # TODO return nlg template saying nope
#             return 1
#         elif intent == "feedback_prompt":
#             # TODO return yes sorry + increment
#             return 1
#
#
# def closing(results):
#     # TODO: if
#     if intent == "greet" or intent == "goodbye":
#         # TODO: before you go, ti chiederei di compilare questo  + link questionario?
#         return 1, "link_to_survey"
#     if intent == "ynq":
#         # TODO: qualcosa con answer_f
#         return 1,


def answering(results):
    pass


def link_to_survey(results):
    pass


def answering_f(results):
    pass


def ans_bidaf(results):
    pass


def dialogue_manager(results):
    """
    Method called by the bot.py to retrieve the information to pass to the NLG
    :param results: dictionary - has: intent, state, entity
    :return: string - text
    """
    if "introduction" in results["state"]:
        return introduction(results)

    # if "storytelling" in results["state"]:
    #     return storytelling(results)
    #
    # if "closing" in results["state"]:
    #     return closing(results)

    if "answering" in results["state"]:
        return answering(results)

    if "link_to_survey" in results["state"]:
        return link_to_survey(results)

    if "answering_f" in results["state"]:
        return answering_f(results)

    if "ans_bidaf" in results["state"]:
        return ans_bidaf(results)

