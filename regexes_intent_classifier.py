from nltk.tokenize import word_tokenize
import nltk
import re


def regex_intent_classifier(text, state_object):

    # check for whq
    question_words = ["WP", "WRB", "WDT", "WP$"]
    verbs = ["VP", "VBZ", "VBP", "VBD", "VBG", "VBN"]

    for q in question_words:
        if q in pos_tag:
            pos_tag = pos_tag.replace(q, "WP")
    for v in verbs:
        if v in pos_tag:
            pos_tag = pos_tag.replace(v, "VRP")

    if re.search(r"\bWP VPP|WP PV\b", pos_tag):
        state_object.intent = "whq"

    else:
        greetings = ["hello", "hi", "ehy", "hey", "ciao", "hola", "what’s up", "good morning", "good afternoon",
                     "good evening", "yo", "howdy", "sup", "hiya"]
        goodbye = ["bye", "goodbye", "see you later", "take care", "see ya"]
        thanks = ["thanks", "thank you", "thnks"]
        yes = ["yes", "yep", "yeah", "yea", "right"]

        for g in greetings:
            if g in text.lower():
                state_object.intent = "greetings"
        for t in thanks:
            if t in text.lower():
                state_object.intent = "thanks"
        for y in yes:
            if y in text.lower():
                state_object.intent = "affirm"
        for gb in goodbye:
            if gb in text.lower():
                state_object.intent = "goodbye"


# if __name__ == '__main__':
#     # text = "don't hello me"
#     state_object = {}
#     # regex_intent_classifier(text, state_object)
#     text2 = "Hellooo!"
#     is_greetings_or_goodbye(text2, state_object)

