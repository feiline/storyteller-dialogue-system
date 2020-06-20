class State:
    def __init__(self, intent, story_told, previous_intent=None):
        self._intent = intent
        self._story_told = [story_told]
        self._previous_intent = previous_intent

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

