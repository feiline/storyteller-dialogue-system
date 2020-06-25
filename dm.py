import random

from nlg import _first_templates, _intro_templates, _goodbye_templates, _storytelling_templates, _closing_templates, \
    _link_to_survey_templates, _answering_templates, _answering_f_templates
from story import depth_first_search


def introduction(state_object):
    """
    Where to find information if state is Introduction
    :param state_object: state object of the bot
    :return: string - text
    """
    intents = ["greetings", "goodbye", "deny", "exclaim_neg", "clarification_request", "ask_if_ended", "feedback_prompt"]
    if state_object.previous_intent == "":
        templates = _first_templates
        return random.choice(templates["intro"])
    else:
        if state_object.previous_intent == "goodbye" or state_object.previous_intent == "deny" \
                or state_object.previous_intent == "exclaim_neg":
            templates = _goodbye_templates
            return random.choice(templates["goodbye"])
        else:
            templates = _intro_templates
            return random.choice(templates[state_object.intent])


def storytelling(state_object):
    """
    Where to find information if state is storytelling
    :param state_object: dictionary with info
    :return: string - text
    """
    # create arguments for the depth_first_Search
    visited = state_object.story_told
    story_graph = state_object.story_graph
    first_node = state_object.current_node
    is_ended = state_object.is_story_ended
    nodes_to_visit = state_object.nodes_to_visit

    # do the depth_first_search to find the story increment to tell next
    node_name, text = depth_first_search(visited, story_graph, first_node, nodes_to_visit, is_ended)
    # save last visited node and update is_ended
    state_object.current_node = node_name
    state_object.is_story_ended = is_ended

    # rules:
    template_fillers = {'text': text}
    templates = _storytelling_templates
    curr_templates = templates[state_object.intent]
    template = random.choice(curr_templates)
    return template.format(**template_fillers)


def closing(state_object):
    """
    retrieve the information to give to the user after the story is told
    :param state_object: state object
    :return: string - text
    """
    if state_object.current_node == "sentence12":
        state_object.current_node == ""
        templates = _closing_templates
        return random.choice(templates["intro"])


def link_to_survey():
    templates = _link_to_survey_templates
    return random.choice(templates["link"])


def answering(state_object):
    templates = _answering_templates
    if "what" in state_object.utterance.lower():
        if "do" in state_object.utterance.lower() or "can" in state_object.utterance.lower() or \
                "could" in state_object.utterance.lower() or "shall" in state_object.utterance.lower() \
                or "should" in state_object.utterance.lower():
            if "i" in state_object.utterance.lower():
                random.choice(templates["what_i_do"])
            elif "you" in state_object.utterance.lower():
                random.choice(templates["what_you_do"])
            elif "we" in state_object.utterance.lower():
                random.choice(templates["what_we_do"])
            else:
                random.choice(templates["what_ot_know"])
        elif "are" in state_object.utterance.lower():
            if "you" in state_object.utterance.lower():
                random.choice(templates["what_are_you"])
            else:
                random.choice(templates["what_ot_know"])
        elif "story" in state_object.utterance.lower():
            random.choice(templates["story"])
        else:
            random.choice(templates["what_ot_know"])
    else:
        random.choice(templates["what_ot_know"])


def answering_f(state_object):
    templates = _answering_f_templates
    if "what" in state_object.utterance.lower():
        if "do" in state_object.utterance.lower() or "can" in state_object.utterance.lower() or \
                "could" in state_object.utterance.lower() or "shall" in state_object.utterance.lower() \
                or "should" in state_object.utterance.lower():
            if "i" in state_object.utterance.lower():
                random.choice(templates["what_i_do"])
            elif "you" in state_object.utterance.lower():
                if "think" in state_object.utterance.lower():
                    random.choice(templates["think"])
        else:
            random.choice(templates["what_ot_know"])
    else:
        random.choice(templates["what_ot_know"])


def ans_bidaf(state_object):
    # TODO: modify to call BIDAF. for now it says it does not know.
    templates = _answering_f_templates
    random.choice(templates["what_ot_know"])
    pass


def dialogue_manager(stateObject, stateMachine):
    """
    Method called by the bot.py to retrieve the information to pass to the NLG
    :param stateObject: state object, in which are stores: intent, previous intent, story graph, nodes visited
    :param stateMachine: finate state machine, in which is stored the current state
    :return: string - text
    """

    current_State = stateMachine.state
    if "introduction" in current_State:
        return introduction(stateObject)

    if "storytelling" in current_State:
        return storytelling(stateObject)

    if "closing" in current_State:
        return closing(stateObject)

    if "answering" in current_State:
        return answering(stateObject)

    if "link_to_survey" in current_State:
        return link_to_survey()

    if "answering_f" in current_State:
        return answering_f(stateObject)

    if "ans_bidaf" in current_State:
        return ans_bidaf(stateObject)

