class State:
    def __init__(self, story_graph, story_told, intent, previous_intent=None):
        self._story_graph = story_graph
        self._story_told = [story_told]
        self._intent = intent
        self._previous_intent = previous_intent
        self.is_story_ended = False

    @property
    def intent(self):
        return self._intent

    @property
    def story_told(self):
        return self._story_told

    @property
    def previous_intent(self):
        return self._intent

    @intent.setter
    def intent(self, new_intent):
        self._intent = new_intent

    @previous_intent.setter
    def previous_intent(self, new_previous_intent):
        self._previous_intent = new_previous_intent

    def add_increment_told(self, new_story_increment):
        self._story_told.append(new_story_increment)

    def set_new_state(self, fsm):
        """
        Given the current state and the intent, the aim is to throw an action to change
        the current state. It returns the new state in which the bot is in.
        :param fsm: object from class ConversationFMS
        :param intent: String - current user intent
        :param is_ended: boolean - is the story finished?
        :return: void - set new current fsm state
        """
        state = fsm.state
        if state == "introduction":
            if self.previous_intent == "":
                fsm.no_change()  # new state: introduction
            else:
                if self.intent == "ynq" or self.intent == "whq":
                    fsm.question()  # new state: answering
                elif self.intent == "affirm" or self.intent == "request_increment" or self.intent == "exclaim_pos"\
                        or self.intent == "ask_for_story" or self.intent == "thanks":
                    fsm.acceptance()  # new state: storytelling
                else:
                    fsm.no_change()  # new state: introduction

        elif state == "storytelling":
            if self.is_story_ended:
                fsm.story_ends()  # new state: closing
            elif self.intent == "ynq" or self.intent == "whq":
                fsm.question()  # new state: bidaf_answering
            else:
                fsm.non_question()  # new state: storytelling

        elif state == "closing":
            if self.intent == "ynq" or self.intent == "whq":
                fsm.question()  # new state: answering_f
            else:
                fsm.acceptance()  # new state: link_to_survey

        elif state == "answering":
            if self.intent == "ask_for_story" or self.intent == "request_increment":
                fsm.ask_increment()  # new state: storytelling
            elif self.intent == "ynq" or self.intent == "whq":
                fsm.question()  # new state: answering
            else:
                fsm.acceptance()  # new state: introduction

        elif state == "ans_bidaf":
            if self.intent == "ynq" or self.intent == "whq":
                fsm.question()  # new state: ans_bidaf
            else:
                fsm.acceptance()  # new state: storytelling

        elif state == "answering_f":
            if self.intent == "ynq" or self.intent == "whq":
                fsm.question()  # new state: answering_f
            else:
                fsm.acceptance()  # new state: link_to_survey
