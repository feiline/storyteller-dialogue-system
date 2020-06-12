from rasa.nlu.model import Interpreter


def get_intent(utterance):
    model = "rasa_nlu/models/nlu"

    interpreter = Interpreter.load(model)
    interpretation = interpreter.parse(utterance)

    return interpretation

# if __name__ == "__main__":
#     utterance = "Hello, world!"
#     intent = get_intent(utterance)
#     print(intent)