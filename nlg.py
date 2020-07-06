class NLG:
    def __init__(self):
        self._first_templates = {
            "intro": [
                "Hello, I would like to tell you a story.",
                "Hello, would you like to hear a story?",
                "Hi, I'm here to tell you a story."
            ]
        }
        self._goodbye_templates = {
            "goodbye": [
                "You can close the windows to proceed or you can write 'yes' to continue with the story.",
                "Ok. You can now close the windows or if you changed your mind you can write 'yes' to continue with "
                "the story."
            ]
        }
        self._intro_templates = {
            "greet": [
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
        self._storytelling_templates = {
            "greet": ["{text}"],
            "goodbye": ["{text}"],
            "affirm": ["{text}"],
            "deny": ["{text}"],
            "whq": ["{text}"],
            "ynq": ["{text}"],
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
        self._closing_templates = {
            "intro": [
                "The end! Hope you enjoyed the story",
                "That's it, hope you enjoyed.",
                "And this is my story, I hope you enjoyed."
            ]
        }

        self._link_to_survey_templates = {
            "link": [
                "Here you can find the link to a quick survey: https://forms.gle/tiBgZrWYJArCiZ7CA",
                "Please find the link to a quick survey here: https://forms.gle/tiBgZrWYJArCiZ7CA",
                "Thanks for listening. Here you can find the link to a quick survey: https://forms.gle/tiBgZrWYJArCiZ7CA"
            ],
            "thanks": [
                "You're welcome. Please fill the survey: https://forms.gle/tiBgZrWYJArCiZ7CA"
            ],
            "smile": [
                ":)",
                "(:"
            ]
        }
        self._answering_templates = {
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
                "Sorry, I can't answer that. Would you like to hear the story?",
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
        self._answering_f_templates = {
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
        self._ans_bert_templates = {
            "whq": ["{text}"],
            "ynq": ["{text}"],
            "greet": ["{text}"],
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

    @property
    def first_templates(self):
        return self._first_templates

    @property
    def intro_templates(self):
        return self._intro_templates

    @property
    def answering_templates(self):
        return self._answering_templates

    @property
    def answering_f_templates(self):
        return self._answering_f_templates

    @property
    def ans_bert_templates(self):
        return self._ans_bert_templates

    @property
    def storytelling_templates(self):
        return self._storytelling_templates

    @property
    def closing_templates(self):
        return self._closing_templates

    @property
    def link_to_survey_templates(self):
        return self._link_to_survey_templates

    @property
    def goodbye_templates(self):
        return self._goodbye_templates
