from transitions import Machine

class Conversation(object):

    # define states
    states = ['introduction', 'storytelling', 'closing', 'answering', 'link_to_survey', 'answering_f']

    def __init__(self, id):
        self.id = id
        self.machine = Machine(model=self, states=Conversation.states, initial='introduction')

        # ----------- TRANSITIONS ------------ #

        # ---- Transition from introduction --- #
        self.machine.add_transition('acceptance', 'introduction', 'storytelling')
        self.machine.add_transition('question', 'introduction', 'answering')

        # ---- Transition from storytelling --- #
        self.machine.add_transition('story_ends', 'storytelling', 'closing')
        self.machine.add_transition('question', 'storytelling', 'bidaf_answering')
        self.machine.add_transition('non-questions', 'storytelling', 'closing', conditions='story_ended')
        self.machine.add_transition('non-questions', 'storytelling', 'storytelling')

        # ---- Transition from answering --- #
        self.machine.add_transition('acceptance', 'answering', 'introduction')
        self.machine.add_transition('question', 'answering', 'answering')
        self.machine.add_transition('ask_increment', 'answering', 'storytelling')

        # ---- Transition from bidaf_answering --- #
        self.machine.add_transition('non_question', 'bidaf_answering', 'storytelling')
        self.machine.add_transition('non_question', 'bidaf_answering', 'closing', conditions='story_ended')
        self.machine.add_transition('question', 'bidaf_answering', 'bidaf_answering')

        # ---- Transition from closing --- #
        self.machine.add_transition('acceptance', 'closing', 'link_to_survey')
        self.machine.add_transition('question', 'closing', 'answering_f')

        # ---- Transition from answering_f --- #
        self.machine.add_transition('question', 'answering_f', 'answering_f')



if __name__ == "__main__":
    conv1 = Conversation('1')
    print("This is the initial state: ", conv1.state)
    conv1.acceptance()
    print("This is the state after 'acceptance' from the user: ", conv1.state)
    conv1.story_ends()
    print("This is the state after 'story_ends': ", conv1.state)

