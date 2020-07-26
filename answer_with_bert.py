import tensorflow as tf
from transformers import BertTokenizer, TFBertForQuestionAnswering


def get_bert_model():
    model = TFBertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    return model


def get_bert_answer(model, question):
    text = "This is one of those times I wish I had a digital camera. We keep a large stainless bowl of water outside" \
           " the house for Benjamin to drink off. His bowl has become a very popular site. " \
           "Throughout the day, many birds drink out of it and bathe in it." \
           " The birds literally line up on the railing and wait their turn. Squirrels also go to drink there." \
           " A squirrel that acted in a very crazy way just came by. He was literally jumping in fright at " \
           "what I believe was his own reflection in the bowl. He was startled so much at one" \
           " point that he leaps in the air and fell off the deck. " \
           " I saw his one little paw hanging on! After a moment or two his paw slipped and he " \
           "tumbled down a few feet. But oh, you should have seen the look on his startled face" \
           " and how he jumped back each time he caught his reflection in the bowl!"

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    encoding = tokenizer.encode_plus(question, text)
    input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]
    start_scores, end_scores = model(tf.constant(input_ids)[None, :],
                                     token_type_ids=tf.constant(token_type_ids)[None, :])
    all_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    answer = ' '.join(all_tokens[tf.math.argmax(tf.squeeze(start_scores)): tf.math.argmax(tf.squeeze(end_scores)) + 1])
    return answer


# --------------- for DEBUG porpuse only ----------------- #
# if __name__ in "__main__":
#     model = get_bert_model()
#     question = "why do you wish to have a camera?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "who is benjamin?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "why is the bowl popular?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "was the squirrel hurt?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "why was the squirrel afraid?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "what happened after a few moments?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "what should I have seen?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "was it that nice?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "wait what?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "what?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "where?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "why?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "when?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)
#     question = "what?"
#     answer = get_bert_answer(model, question)
#     print(question, answer)