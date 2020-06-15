from rasa.nlu.model import Interpreter


def get_intent(utterance):
    """
    retrieves intent from user utterance
    :param utterance: String - user utterance
    :return: string - intent
    """
    model = "rasa_nlu/models/nlu"

    interpreter = Interpreter.load(model)
    interpretation = interpreter.parse(utterance)

    return interpretation


def set_new_state(fsm, intent, is_ended):
    """
    Given the current state and the intent, the aim is to throw an action to change
    the current state. It returns the new state in which the bot is in.
    :param fsm: object from class ConversationFMS
    :param intent: String - current user intent
    :param is_ended: boolean - is the story finished?
    :return: void - set new current fsm state
    """
    state = fsm.state
    if state == "Introduction":
        if intent == "ynq" or intent == "whq":
            fsm.question()  # new state: answering
        else:
            fsm.acceptance()  # new state: storytelling

    elif state == "storytelling":
        if is_ended:
            fsm.story_ends()  # new state: closing
        elif intent == "ynq" or intent == "whq":
            fsm.question()  # new state: bidaf_answering
        else:
            fsm.non_question()  # new state: storytelling if is_ended = false

    elif state == "closing":
        if intent == "ynq" or intent == "whq":
            fsm.question()  # new state: answering_f
        else:
            fsm.acceptance()  # new state: link_to_survey

    elif state == "answering":
        if intent == "ask_for_story" or intent == "request_increment":
            fsm.ask_increment()  # new state: storytelling
        elif intent == "ynq" or intent == "whq":
            fsm.question()  # new state: answering
        else:
            fsm.acceptance() # new state: introduction

    elif state == "ans_bidaf":
        if intent == "ynq" or intent == "whq":
            fsm.question()  # new state: ans_bidaf
        else:
            fsm.acceptance()  # new state: storytelling if is_finished = false, closing if is_finished = true

    elif state == "answering_f":
        if intent == "ynq" or intent == "whq":
            fsm.question()  # new state: answering_f
        else:
            fsm.acceptance()  # new state: link_to_survey


# if __name__ == "__main__":
#     utterance = "Hello, world!"
#     nluResult = get_intent(utterance)
#     intent = nluResult["intent"]["name"]
#     print(intent)
