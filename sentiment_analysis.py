import random
import re
import string

from nltk import FreqDist, NaiveBayesClassifier
from nltk.corpus import twitter_samples, stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tag import pos_tag


def remove_noise(tweet_tokens, stop_words = ()):
    cleaned_tokens = []
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
        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


def get_classifier():
    stop_words = stopwords.words('english')
    positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
    negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')
    positive_cleaned_tokens_list = []
    negative_cleaned_tokens_list = []
    for tokens in positive_tweet_tokens:
        positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))
    for tokens in negative_tweet_tokens:
        negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))
    all_pos_words = get_all_words(positive_cleaned_tokens_list)
    # freq_dist_pos = FreqDist(all_pos_words)
    # print(freq_dist_pos.most_common(10))

    positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
    negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)
    positive_dataset = [(tweet_dict, "Positive") for tweet_dict in positive_tokens_for_model]
    negative_dataset = [(tweet_dict, "Negative") for tweet_dict in negative_tokens_for_model]

    dataset = positive_dataset + negative_dataset
    random.shuffle(dataset)
    train_data = dataset[:7000]
    test_data = dataset[7000:]

    classifier = NaiveBayesClassifier.train(train_data)
    # print("Accuracy is:", classify.accuracy(classifier, test_data))
    return classifier

# if __name__ == "__main__":
#     classifier = get_classifier()
#     print(classifier.show_most_informative_features(10))
#     custom_tweet = "sounds like a fable or fairytale"
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "Australia would love to go there"
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "I'd say so and yes its sad that it happens period"
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "I am not seeing any of your messages."
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "Whales are such magnificent creatures. Something I have never seen personally."
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "Have a most wonderful rest of your vacation."
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "It's a good thing the lion let the mouse go then or he would still be in the net"
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "I bet they go there very early to get what they need for their sushi."
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "Im sorry you missed the fresh fish for the day. Perhaps you can learn some Romanji to Engoish words."
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "It's a good thing the lion let the mouse go then or he would still be in the net"
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "Thats what you call loyal to a friend"
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "That is really cool!"
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
#     custom_tweet = "Love morals"
#     custom_tokens = remove_noise(word_tokenize(custom_tweet))
#     print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
