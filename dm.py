# Determina cosa accade in ogni stato.
# Può essere scritto come un univo metodo chiamato da bot.py
# STAI USANDO LA MACCHINA A STATI FINITI
from fms import ConversationFMS


def intro(fsm, intent):
    if intent == "greet":
        # TODO: nlp template
        return "Hello, ready to hear a story?", "introduction"

    elif intent == "affirm" or intent == "exclaim_pos" or intent == "thanks" or intent == "request_increment" \
            or intent == "ask_for_story" or intent == "comment":
        # TODO: nlp template + first phrase of story
        return "Ok, here is my story:", "storytelling"

    elif intent == "ynq" or intent == "whq" or intent == "thanks":
        # TODO: nlp template
        return "NLP TEMPLATE", "introduction"

    elif intent == "feedback_prompt":
        # TODO: nlp template
        return "NLP TEMPLATE", "introduction"

        # TODO: scrivi qualcosa di sensato
    else:
        return "You can type 'yes' to continue.", "introduction"


def storytelling(fsm, intent):
    # TODO check the story is not finished. If finished, that closing
    temp = 1
    if temp != 1:
        # TODO nlg template story is fished
        fsm.story_ends()
        return "template"
    else:
        if intent == "greet" or intent == "affirm" or intent == "deny" or intent == "thanks"\
                or intent == "request_increment" or intent == "comment":
            # TODO: return next piece of information
            return 1
        elif intent == "goodbye":
            # TODO: chiedi se l'utente se ne vuole andare o se continui?
            return 1
        elif intent == "exclaim_neg" or intent == "exclaim_pos":
            # TODO: "IKR?" nlp template + next bit of the story
            return 1
        elif intent == "ynq" or intent == "whq":
            # TODO: call bidaf
            fsm.question()
            return 1
        elif intent == "refocus_topic" or intent == "clarification_request":
            # TODO: return la frase precedente in template nlg
            return 1
        elif intent == "ask_if_ended":
            # TODO: if story ended say yes, if not say no. Add checking to the story
            return 1
        elif intent == "ask_for_story":
            # TODO return nlg template saying nope
            return 1
        elif intent == "feedback_prompt":
            # TODO return yes sorry + increment
            return 1


def closing(fsm, intent):
    # TODO: if
    if intent == "greet" or intent == "goodbye":
        # TODO: before you go, ti chiederei di compilare questo  + link questionario?
        return 1, "link_to_survey"
    if intent == "ynq":
        # TODO: qualcosa con answer_f
        return 1,


def dialogue_manager(fsm, intent):
    if fsm.state == "introduction":
        return intro(fsm, intent)

    if fsm.state == "storytelling":
        return storytelling(fsm, intent)

    if fsm.state == "closing":
        return closing(fsm, intent)

    if fsm.state == "answering":
        return "Once upon a time a princess was born."

    if fsm.state == "link_to_survey":
        return "Once upon a time a princess was born."

    if fsm.state == "answering_f":
        return "Once upon a time a princess was born."

    if fsm.state == "ans_bidaf":
        return "Once upon a time a princess was born."

