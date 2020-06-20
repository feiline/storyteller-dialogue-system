class State:
    def __init__(self, intent, story_told, previous_intent=None):
        self._intent = intent
        self._story_told = story_told
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

    # setter
    def set_intent(self, new_intent):
        self._intent = new_intent

    def add_increment_told(self, new_story_increment):
        self._story_told.append(new_story_increment)

    def set_previous_intent(self):
        self._previous_intent = self._intent


