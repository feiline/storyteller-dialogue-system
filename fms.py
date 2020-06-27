from transitions import Machine


class ConversationFMS(object):

    # define states
    states = ['introduction', 'storytelling', 'closing', 'answering', 'link_to_survey', 'answering_f', 'bert']

    def __init__(self, state):
        self.machine = Machine(model=self, states=ConversationFMS.states, initial=state)

        # ----------- TRANSITIONS ------------ #

        # ---- Transition from introduction --- #
        self.machine.add_transition('acceptance', 'introduction', 'storytelling')
        self.machine.add_transition('question', 'introduction', 'answering')
        self.machine.add_transition('no_change', 'introduction', 'introduction')

        # ---- Transition from storytelling --- #
        self.machine.add_transition('story_ends', 'storytelling', 'closing')
        self.machine.add_transition('question', 'storytelling', 'bert')
        self.machine.add_transition('non_question', 'storytelling', 'storytelling')

        # ---- Transition from answering --- #
        self.machine.add_transition('acceptance', 'answering', 'storytelling')
        self.machine.add_transition('question', 'answering', 'answering')

        # ---- Transition from bert --- #
        self.machine.add_transition('acceptance', 'bert', 'storytelling')
        self.machine.add_transition('story_ends', 'bert', 'closing')
        self.machine.add_transition('question', 'bert', 'bert')

        # ---- Transition from closing --- #
        self.machine.add_transition('acceptance', 'closing', 'link_to_survey')
        self.machine.add_transition('question', 'closing', 'answering_f')

        # ---- Transition from answering_f --- #
        self.machine.add_transition('question', 'answering_f', 'answering_f')
        self.machine.add_transition('acceptance', 'answering_f', 'link_to_survey')


# if __name__ == "__main__":
#     conv1 = ConversationFMS('1')
#     print("This is the initial state: ", conv1.state)
#     conv1.acceptance()
#     print("This is the state after 'acceptance' from the user: ", conv1.state)
#     conv1.story_ends()
#     print("This is the state after 'story_ends': ", conv1.state)
#