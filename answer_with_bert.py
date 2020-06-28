import tensorflow as tf
import time
from transformers import BertTokenizer, TFBertForQuestionAnswering


def get_bert_model():
    model = TFBertForQuestionAnswering.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
    return model


def get_bert_answer(model, question):
    text = "I wish I had a digital camera because something really funny happened " \
           "and I wanted to capture it " \
           "on camera. We keep a large stainless bowl of water outside the house for Benjamin, our dog, to " \
             "drink off. His bowl has become a very popular site, there are often other animals to drink there" \
             "despite being the dog bowl. Throughout the day, many birds drink out of it and bathe in it. " \
             "The birds literally line up on the railing and wait their turn. Squirrels also go to drink there." \
             " A squirrel that acted in a very crazy way just came by. He was literally jumping in fright at " \
             "seeing his own reflection in the bowl, or at least I think so. He was startled so much at one" \
             " point that he leap in the air and fell off the deck, but no worries, the squirrel did not hurt" \
             " himself. I saw his one little paw hanging on! After a moment or two his paw slipped and he " \
             "tumbled down a few feet. It was really fun, you should have seen the look on his startled face" \
             " and how he jumped back each time he caught his reflection in the bowl!"

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    encoding = tokenizer.encode_plus(question, text)
    input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]
    start_scores, end_scores = model(tf.constant(input_ids)[None, :],
                                     token_type_ids=tf.constant(token_type_ids)[None, :])
    all_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    answer = ' '.join(all_tokens[tf.math.argmax(tf.squeeze(start_scores)): tf.math.argmax(tf.squeeze(end_scores)) + 1])
    return answer


if __name__ in "__main__":
    model = get_bert_model()
    question = "why you wish to have a camera?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "who is benjamin?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "why is the bowl popular?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "was the squirrel hurt?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "why was the squirrel afraid?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "what happened after a few moments?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "what should I have seen?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "was it that nice?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "wait what?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "what?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "where?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "why?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "when?"
    answer = get_bert_answer(model, question)
    print(question, answer)
    question = "what?"
    answer = get_bert_answer(model, question)
    print(question, answer)



# for i in range(0, 100):
#     start_time = time.time()
#     question, text = "Who was Jim Henson?", "Jim Henson was a nice puppet"
#     encoding = tokenizer.encode_plus(question, text)
#     input_ids, token_type_ids = encoding["input_ids"], encoding["token_type_ids"]
#
#
#     all_tokens = tokenizer.convert_ids_to_tokens(input_ids)
#     answer = ' '.join(all_tokens[tf.math.argmax(tf.squeeze(start_scores)) : tf.math.argmax(tf.squeeze(end_scores))+1])
#     print(answer)
#     print(1 / (time.time() - start_time), "hz")
