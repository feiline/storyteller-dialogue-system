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


# if __name__ == "__main__":
#     utterance = "I guess this is it"
#     nluResult = get_intent(utterance)
#     intent = nluResult["intent"]["name"]
#     print(intent)
