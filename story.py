import random
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout


class StorySentenceNode:
    def __init__(self, name, sentence, previous_story_sentence_nodes):
        self._name = name
        self._sentence = sentence
        self._previous_story_sentence_nodes = previous_story_sentence_nodes

    @property
    def name(self):
        return self._name

    @property
    def sentence(self):
        return self._sentence

    @property
    def previous_story_sentence_nodes(self):
        return self._previous_story_sentence_nodes


def create_graph(sentence_nodes):
    # create graph
    Graph = nx.DiGraph()
    # add nodes
    for sentence_node in sentence_nodes:
        Graph.add_node(sentence_node.name, node_object=sentence_node)
    # add edges
    for sentence_node in sentence_nodes:
        for dependency_node in sentence_node.previous_story_sentence_nodes:
            Graph.add_edge(dependency_node.name, sentence_node.name)
    return Graph


def get_story_graph():
    DICT_STORY = {'1': "This is one of those times I wish I had a digital camera.",
                  '2': "We keep a large stainless steel bowl of water outside on the back deck for Benjamin "
                       "to drink out of when he's playing outside.",
                  '3': "His bowl has become a very popular site.",
                  '4': "Throughout the day, many birds drink out of it and bathe in it.",
                  '5': "The birds literally line up on the railing and wait their turn.",
                  '6': "Squirrels also come to drink out of it.",
                  '7': "The craziest squirrel just came by-",
                  '8': "he was literally jumping in fright at what I believe was his own reflection in the bowl",
                  '9': "He was startled so much at one point that he leap in the air and fell off the deck.",
                  '10': "But not quite, I saw his one little paw hanging on!",
                  '11': "After a moment or two his paw slipped and he tumbled down a few feet.",
                  '12': "But oh, if you could have seen the look on his startled face and how he jumped back each time "
                       "he caught his reflection in the bowl!"}

    sentence1 = StorySentenceNode("sentence1", DICT_STORY['1'], [])
    sentence2 = StorySentenceNode("sentence2", DICT_STORY['2'], [sentence1])
    sentence3 = StorySentenceNode("sentence3", DICT_STORY['3'], [sentence2])
    sentence4 = StorySentenceNode("sentence4", DICT_STORY['4'], [sentence3])
    sentence5 = StorySentenceNode("sentence5", DICT_STORY['5'], [sentence4])
    sentence6 = StorySentenceNode("sentence6", DICT_STORY['6'], [sentence5])
    sentence7 = StorySentenceNode("sentence7", DICT_STORY['7'], [sentence3])
    sentence8 = StorySentenceNode("sentence8", DICT_STORY['8'], [sentence7])
    sentence9 = StorySentenceNode("sentence9", DICT_STORY['9'], [sentence8])
    sentence10 = StorySentenceNode("sentence10", DICT_STORY['10'], [sentence9])
    sentence11 = StorySentenceNode("sentence11", DICT_STORY['11'], [sentence10])
    sentence12 = StorySentenceNode("sentence12", DICT_STORY['12'], [sentence11])

    sentence_graph = [sentence1, sentence2, sentence3, sentence4, sentence5, sentence6, sentence7, sentence8, sentence9,
                      sentence10, sentence11, sentence12]

    story_graph = create_graph(sentence_graph)
    return story_graph


def depth_first_search(visited, graph, node_name, node_to_visit, is_ended):
    """
    Method to retrieve the next sentence to say - implemented as a depth first search
    :param visited: list of nodes whoch story has been already told in the conversations
    :param graph: story graph
    :param node_name: node in which is stored the first story increment
    :return: next increment based on what has been already told to the user
    """
    nodes = ['sentence1', 'sentence2', 'sentence3', 'sentence4', 'sentence5', 'sentence6', 'sentence7', 'sentence8',
             'sentence9', 'sentence10', 'sentence11', 'sentence12']

    # if the node contains the last increment of the story
    if node_name == "sentence12":
        is_ended = True
        return node_name, graph.nodes[node_name]["node_object"].sentence

    else:
        if node_name not in visited:
            visited.append(node_name)
            return node_name, graph.nodes[node_name]["node_object"].sentence

        elif len(graph.adj[node_name]) > 0:
            next_nodes = graph.adj[node_name]
            if len(next_nodes) > 1:
                if "sentence7" in node_to_visit:
                    next_node = "sentence7"
                elif "sentence4" in node_to_visit:
                    next_node = "sentence4"
                else:
                    for node in nodes:
                        if node in next_nodes:
                            node_to_visit.append(node)
                    next_node = random.choice(node_to_visit)
                    node_to_visit.remove(next_node)
                return depth_first_search(visited, graph, next_node, node_to_visit, is_ended)
            else:
                for node in nodes:
                    if node in next_nodes:
                        next_node = node
                return depth_first_search(visited, graph, next_node, node_to_visit, is_ended)

        else:
            next_node = random.choice(node_to_visit)
            node_to_visit.remove(next_node)
            return depth_first_search(visited, graph, next_node, node_to_visit, is_ended)


# --------------------------- DEBUGGING PURPOSES ONLY ------------------------ #
#
# def main():
#     story_graph = get_story_graph()
#     visited_nodes = []
#     nodes_to_visit = []
#     first_node = "sentence1"
#     for i in range(13):
#         node_name, answer = depth_first_search(visited_nodes, story_graph, first_node, nodes_to_visit, is_ended=False)
#         first_node = node_name
#         print(answer)

#     pos = graphviz_layout(graph, prog='dot')
#     labels = {v.name: v.name for v in sentence_graph}
#     nx.draw(graph, with_labels=True, pos=pos, labels=labels)
#     plt.show()

#
# if __name__ == "__main__":
#     main()
