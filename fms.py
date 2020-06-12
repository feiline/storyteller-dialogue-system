from transitions import Machine

class Conversation(object):

    # define states
    states = ['introduction', 'storytelling', 'closing']

    def __init__(self, id):
        self.id = id
        self.machine = Machine(model=self, states=Conversation.states, initial='introduction')

        # transitions
        self.machine.add_transition('acceptance', 'introduction', 'storytelling')
        self.machine.add_transition('story_ends', 'storytelling', 'closing')

if __name__ == "__main__":
    conv1 = Conversation('1')
    print("This is the initial state: ", conv1.state)
    conv1.acceptance()
    print("This is the state after 'acceptance' from the user: ", conv1.state)
    conv1.story_ends()
    print("This is the state after 'story_ends': ", conv1.state)

