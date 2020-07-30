import random
import re
import string

from nltk import word_tokenize, NaiveBayesClassifier, classify
from nltk.corpus import twitter_samples, stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag


def remove_noise(tweet_tokens, stop_words=()):
    clean_tokens = []
    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)
        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)
        if len(token) > 0:
            if token not in string.punctuation:
                if token.lower() not in stop_words:
                    clean_tokens.append(token.lower())
    return clean_tokens


def get_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets(clean_tokens_list):
    for t_tokens in clean_tokens_list:
        yield dict([token, True] for token in t_tokens)


def get_classifier():
    p_clean_tokens = []
    n_clean_tokens = []
    stop_words = stopwords.words('english')
    p_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    n_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')
    for tokens in p_tweet_tokens:
        p_clean_tokens.append(remove_noise(tokens, stop_words))
    for tokens in n_tweet_tokens:
        n_clean_tokens.append(remove_noise(tokens, stop_words))

    p_tokens = get_tweets(p_clean_tokens)
    n_tokens = get_tweets(n_clean_tokens)
    p_dataset = [(tweet_dict, "Positive") for tweet_dict in p_tokens]
    n_dataset = [(tweet_dict, "Negative") for tweet_dict in n_tokens]

    data = p_dataset + n_dataset
    random.shuffle(data)
    train_x = data[:7000]
    test_x = data[7000:]

    model = NaiveBayesClassifier.train(train_x)
    print("The accuracy is:", classify.accuracy(model, test_x))
    return model


if __name__ == "__main__":
    model = get_classifier()
#     print(model.show_most_informative_features(10))
#     utterance = "sounds like a fable or fairytale"
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "Australia would love to go there"
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "I'd say so and yes its sad that it happens period"
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "I am not seeing any of your messages."
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "Whales are such magnificent creatures. Something I have never seen personally."
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "Have a most wonderful rest of your vacation."
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "It's a good thing the lion let the mouse go then or he would still be in the net"
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "I bet they go there very early to get what they need for their sushi."
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "Im sorry you missed the fresh fish for the day. Perhaps you can learn some Romanji to Engoish words."
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "It's a good thing the lion let the mouse go then or he would still be in the net"
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "Thats what you call loyal to a friend"
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "That is really cool!"
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
#     utterance = "Love morals"
#     tokens = remove_noise(word_tokenize(utterance))
#     print(utterance, model.classify(dict([token, True] for token in tokens)))
