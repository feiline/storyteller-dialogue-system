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
        self._storytelling_s1_templates = {
            "sentence1": ["{acknowledge} {text} Do you know why?"],
            "sentence2": ["{acknowledge} {text} All clear so far?"],
            "sentence3": ["{acknowledge} {text}. Would you like to try and guess why?"],
            "sentence4": ["{acknowledge} {text}"],
            "sentence5": [
                "{acknowledge} {text} Amazing, right?",
                "{acknowledge} {text} I think it's amazing!"
            ],
            "sentence6": [
                "{acknowledge} {text} Aren't they lovely?",
                "{acknowledge} {text} I'm so lucky to have them in the garden, right?"
            ],
            "sentence7": [
                "{acknowledge} {text}",
                "{acknowledge} {text}"
            ],
            "sentence8pos": ["{acknowledge} {text}"],
            "sentence8neg": ["{acknowledge} {text}"],
            "sentence9": ["{acknowledge} {text}"],
            "sentence10": ["{acknowledge} {text}"]
        }
        self._closing_templates = {
            "intro": [
                "The end! Hope you enjoyed the story",
                "That's it, hope you enjoyed.",
                "And this is my story, I hope you enjoyed."
            ]
        }

        self._closing_templates_s1 = {
            "intro_pos": [
                "The end! I hope you enjoyed the story",
                "That's it, I hope you enjoyed.",
                "And this is my story, I hope you enjoyed."
            ]
        }

        self._link_to_survey_templates_s1 = {
            "link": [
                "Here you can find the link to a quick survey: https://forms.gle/uTbw629utDPjNWYU6",
                "Please find attached the link to a quick survey here: https://forms.gle/uTbw629utDPjNWYU6",
                "Thanks for listening. Here you can find the link to a quick survey: https://forms.gle/uTbw629utDPjNWYU6"
            ],
            "thanks": [
                "You're welcome. Please fill the survey: https://forms.gle/uTbw629utDPjNWYU6"
            ],
            "smile": [
                ":)",
                "(:"
            ]
        }

        self._link_to_survey_templates = {
            "link": [
                "Here you can find the link to a quick survey: https://forms.gle/ntwGDa3y8nxGG1w57",
                "Please find attached the link to a quick survey here: https://forms.gle/ntwGDa3y8nxGG1w57",
                "Thanks for listening. Here you can find the link to a quick survey: https://forms.gle/ntwGDa3y8nxGG1w57"
            ],
            "thanks": [
                "You're welcome. Please fill the survey: https://forms.gle/ntwGDa3y8nxGG1w57"
            ],
            "smile": [
                ":)",
                "(:"
            ]
        }
        self._answering_templates = {
            "what_i_do": [
                "I am not sure. I just know I have this story to tell you.",
                "I am not sure, sorry. But I know this story, would you like to hear it?",
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
            "what_to_know": [
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
        self._ans_bert_s1_templates = {
            "whq": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "ynq": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "greet": [
                "{text}. Makes sense?",
                "{text}"

            ],
            "goodbye": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "affirm": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "deny": [
                "{text}. Makes sense?",
                "{text}"

            ],
            "exclaim_neg": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "exclaim_pos": [
                "{text}. Makes sense?",
                "{text}. Did I answer you?",
                "{text}. Was this the answer you were looking for?",
                "{text}. You asked me this, right?"
            ],
            "thanks": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "request_increment": [
                    "{text}. Makes sense?",
                    "{text}"
            ],
            "clarification_request": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "ask_if_ended": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "ask_for_story": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "comment": [
                "{text}. Makes sense?",
                "{text}"
            ],
            "feedback_prompt": [
                "{text}. Makes sense?",
                "{text}"
            ],
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
    def ans_bert_s1_templates(self):
        return self._ans_bert_s1_templates

    @property
    def storytelling_templates(self):
        return self._storytelling_templates

    @property
    def storytelling_s1_templates(self):
        return self._storytelling_s1_templates

    @property
    def closing_templates(self):
        return self._closing_templates

    @property
    def link_to_survey_templates(self):
        return self._link_to_survey_templates

    @property
    def link_to_survey_templates_s1(self):
        return self._link_to_survey_templates_s1

    @property
    def goodbye_templates(self):
        return self._goodbye_templates
