import random
import sys
import logging

logger = logging.getLogger(__name__)

_first_templates = {
    "intro": [
        "Hello, I would like to tell you a story.",
        "Hello, would you like to hear a story?",
        "Hi, I'm here to tell you a story."
    ]
}

_goodbye_templates = {
    "goodbye": [
        "You can close the windows to proceed or you can write 'yes' to continue with the story.",
        "Ok. You can now close the windows or if you changed your mind you can write 'yes' to continue with the story."
    ]
}

_intro_templates = {
    "greetings": [
        "Hello again! Ready for the story?",
        "Hello hello, shall I begin?",
        "Well hello again, would you like to hear the story?",
    ],
    "goodbye": ["Wait, no story? It's short I promise."],
    "deny": ["Wait, no story? It's short I promise."],
    "exclaim_neg": ["Wait, no story? It's short I promise."],
    "clarification_request": ["I will tell you a story that I know. Shall I start?"],
    "ask_if_ended": ["It is not started yet. Shall I start?"],
    "feedback_prompt": [
        "Yes, sorry. Are you here for a story?"
        "I'm here. Would you like to hear a story?"
    ]
}

_storytelling_templates = {
    "greetings": ["{text}"],
    "goodbye": ["{text}"],
    "affirm": ["{text}"],
    "deny": ["{text}"],
    "exclaim_neg": ["{text}"],
    "exclaim_pos": ["{text}"],
    "thanks": ["{text}"],
    "request_increment": ["{text}"],
    "clarification_request": ["{text}"],
    "ask_if_ended": ["{text}"],
    "ask_for_story": ["{text}"],
    "comment": ["{text}"],
    "feedback_prompt": ["{text}"],
}

_closing_templates = {
    "intro": [
        "The end.",
        "That's it, hope you enjoyed.",
        "Story ended."
        ]
}

_link_to_survey_templates = {
    "link": [
        "Here you can find the link to a quick survey: *link*",
        "Please find the link to a quick survey here: *link*",
        "Thanks for listening. Here you can find the link to a quick survey: *link*"
    ]
}

_answering_templates = {
    "what_i_do": [
        "I am not sure. I just know I have this story to tell you.",
        "I an not sure, sorry. But I know this story, would you like to hear it?",
    ],
    "what_you_do": [
        "I'm here to tell you a brief story. Ready to hear it?",
        "I'm a storyteller. Would you like to hear the story?"
    ],
    "what_we_do": [
        "Well, there is this story that I would like to tell you. Ready?",
        "Just talk. I have this story to tell."
    ],
    "what_ot_know": [
        "Sorry, I didn't catch that. Would you like to hear the story?",
        "I don't think I know the answer. Would you like to hear the story?"
    ],
    "what_are_you": [
        "I am a storyteller bot.",
        "I am a storyteller."
    ],
    "story": [
        "You'll see in a moment. Shall I start?",
        "You'll discover it soon. Shall I start?"
    ]
}

_answering_f_templates = {
    "what_i_do": [
        "You can now take a survey.",
        "Please take the survey I will send you."
    ],
    "think": [
        "I think the story is funny.",
        "I think the story is funny, but poor squirrel."
    ],
    "what_ot_know": [
        "Sorry, I didn't catch that."
    ]
}

_ans_bert_templates = {
    "whq":  ["{text}"],
    "ynq":  ["{text}"],
    "greetings": ["{text}"],
    "goodbye": ["{text}"],
    "affirm": ["{text}"],
    "deny": ["{text}"],
    "exclaim_neg": ["{text}"],
    "exclaim_pos": ["{text}"],
    "thanks": ["{text}"],
    "request_increment": ["{text}"],
    "clarification_request": ["{text}"],
    "ask_if_ended": ["{text}"],
    "ask_for_story": ["{text}"],
    "comment": ["{text}"],
    "feedback_prompt": ["{text}"],
}

# if __name__ == "__main__":
#     results = {
#         "intent": {},
#         "entity": {},
#         "pointer_story": {},
#         "text": {}
#     }
#     drivers = StorytellerGenerator()
#     print(drivers.fill_template(results))