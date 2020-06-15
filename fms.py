from transitions import Machine


class ConversationFMS(object):

    # define states
    states = ['introduction', 'storytelling', 'closing', 'answering', 'link_to_survey', 'answering_f', 'ans_bidaf']

    def __init__(self, state):
        self.machine = Machine(model=self, states=ConversationFMS.states, initial=state)

        # ----------- TRANSITIONS ------------ #

        # ---- Transition from introduction --- #
        self.machine.add_transition('acceptance', 'introduction', 'storytelling')
        self.machine.add_transition('question', 'introduction', 'answering')

        # ---- Transition from storytelling --- #
        self.machine.add_transition('story_ends', 'storytelling', 'closing')
        self.machine.add_transition('question', 'storytelling', 'bidaf_answering')
        self.machine.add_transition('non_question', 'storytelling', 'closing', conditions='story_ended')
        self.machine.add_transition('non_question', 'storytelling', 'storytelling')

        # ---- Transition from answering --- #
        self.machine.add_transition('acceptance', 'answering', 'introduction')
        self.machine.add_transition('question', 'answering', 'answering')
        self.machine.add_transition('ask_increment', 'answering', 'storytelling')

        # ---- Transition from ans_bidaf --- #
        self.machine.add_transition('acceptance', 'ans_bidaf', 'storytelling')
        self.machine.add_transition('acceptance', 'ans_bidaf', 'closing', conditions='story_ended')
        self.machine.add_transition('question', 'ans_bidaf', 'ans_bidaf')

        # ---- Transition from closing --- #
        self.machine.add_transition('acceptance', 'closing', 'link_to_survey')
        self.machine.add_transition('question', 'closing', 'answering_f')

        # ---- Transition from answering_f --- #
        self.machine.add_transition('question', 'answering_f', 'answering_f')
        self.machine.add_transition('acceptance', 'answering_f', 'link_to_survey')


if __name__ == "__main__":
    conv1 = ConversationFMS('1')
    print("This is the initial state: ", conv1.state)
    conv1.acceptance()
    print("This is the state after 'acceptance' from the user: ", conv1.state)
    conv1.story_ends()
    print("This is the state after 'story_ends': ", conv1.state)

