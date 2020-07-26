from rasa.nlu.model import Interpreter


def get_model():
    model = "rasa_nlu/models/nlu"

    interpreter = Interpreter.load(model)
    return interpreter


def get_intent(interpreter, utterance):
    """
    retrieves intent from user utterance
    :param interpreter: rasa model
    :param utterance: String - user utterance
    :return: string - intent
    """
    interpretation = interpreter.parse(utterance)
    return interpretation

# if __name__ == "__main__":
#     utterances = ["I guess this is it", "Yes", "Thank you very much", "so what happened?", "oh no, did he survive?",
#                   "bye, see you next time", "and then?", "ok", "not really", "wow that's nice!!"]
#     interpreter = get_model()
#     for i in range(0, 100):
#         start_time = time.time()
#         nluResult = get_intent(interpreter, random.choice(utterances))
#         intent = nluResult["intent"]["name"]
#         print(intent)
#         print(1 / (time.time() - start_time), "hz")