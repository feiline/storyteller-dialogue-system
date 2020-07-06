import random

from answer_with_bert import get_bert_answer
from nlg import NLG
from story import depth_first_search


def introduction(state_object, nlg_object):
    """
    Where to find information if state is Introduction
    :param nlg_object: nlg object with nlp templates
    :param state_object: state object of the bot
    :return: string - text
    """
    intents = ["greet", "goodbye", "deny", "exclaim_neg", "clarification_request", "ask_if_ended", "feedback_prompt"]
    if state_object.previous_intent == "":
        templates = nlg_object.first_templates
        return random.choice(templates["intro"])
    else:
        if state_object.previous_intent == "goodbye" or state_object.previous_intent == "deny" \
                or state_object.previous_intent == "exclaim_neg":
            templates = nlg_object.goodbye_templates
            return random.choice(templates["goodbye"])
        else:
            templates = nlg_object.intro_templates
            return random.choice(templates[state_object.intent])


def storytelling(state_object, nlg_object):
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
    templates = nlg_object.storytelling_templates
    curr_templates = templates[state_object.intent]
    template = random.choice(curr_templates)
    return template.format(**template_fillers)


def closing(state_object, nlg_object):
    """
    retrieve the information to give to the user after the story is told
    :param state_object: state object
    :return: string - text
    """
    if state_object.current_node == "sentence10":
        state_object.current_node == ""
        templates = nlg_object.closing_templates
        return random.choice(templates["intro"])


def link_to_survey(state_object, nlg_object):
    templates = nlg_object.link_to_survey_templates
    if state_object.intent == "thanks":
        return random.choice(templates["thanks"])
    elif state_object.previous_intent == "thanks":
        return random.choice(templates["smile"])
    else:
        return random.choice(templates["link"])


def answering(state_object, nlg_object):
    templates = nlg_object.answering_templates
    if "what" in state_object.utterance.lower():
        if "do" in state_object.utterance.lower() or "can" in state_object.utterance.lower() or \
                "could" in state_object.utterance.lower() or "shall" in state_object.utterance.lower() \
                or "should" in state_object.utterance.lower():
            if "i" in state_object.utterance.lower():
                return random.choice(templates["what_i_do"])
            elif "you" in state_object.utterance.lower():
                return random.choice(templates["what_you_do"])
            elif "we" in state_object.utterance.lower():
                return random.choice(templates["what_we_do"])
            else:
                return random.choice(templates["what_ot_know"])
        elif "are" in state_object.utterance.lower():
            if "you" in state_object.utterance.lower():
                return random.choice(templates["what_are_you"])
            else:
                return random.choice(templates["what_ot_know"])
        elif "story" in state_object.utterance.lower():
            return random.choice(templates["story"])
        else:
            return random.choice(templates["what_ot_know"])
    elif "who" in state_object.utterance.lower():
        if "are" in state_object.utterance.lower():
            if "you" in state_object.utterance.lower():
                return random.choice(templates["what_are_you"])
            else:
                return random.choice(templates["what_ot_know"])
    else:
        return random.choice(templates["what_ot_know"])


def answering_f(state_object, nlg_object):
    templates = nlg_object.answering_f_templates
    if "what" in state_object.utterance.lower():
        if "do" in state_object.utterance.lower() or "can" in state_object.utterance.lower() or \
                "could" in state_object.utterance.lower() or "shall" in state_object.utterance.lower() \
                or "should" in state_object.utterance.lower():
            if "i" in state_object.utterance.lower():
                return random.choice(templates["what_i_do"])
            elif "you" in state_object.utterance.lower():
                if "think" in state_object.utterance.lower():
                    return random.choice(templates["think"])
        else:
            return random.choice(templates["what_ot_know"])
    else:
        return random.choice(templates["what_ot_know"])


def ans_bert(state_object, nlg_object):
    text = get_bert_answer(state_object.bert_model, state_object.utterance)
    utterance = state_object.utterance.lower()
    answers = ["I am afraid I don't remember.", "I am not sure."]
    if "why" in utterance:
        if "sentence3" in state_object.current_node:
            text = "Because of the water, many animals come to drink there."
        elif "sentence1" in state_object.current_node:
            text = "Because something interesting happened and I wanted to capture it on camera."
        elif "sentence5" in state_object.current_node:
            text = "To drink."
        elif "sentence1" in state_object.current_node:
            text = "Because something interesting happened and I wanted to capture it on camera."
        else:
            text = random.choice(answers)
    elif "SEP" in text:
        text = random.choice(answers)
    elif text == "":
        if "sentence2" in state_object.current_node:
            if "who" in utterance or "benjamin" in utterance or "ben" in utterance:
                text = "Benjamin is our dog."
        else:
            text = random.choice(answers)
    elif "what" in utterance:
        return "next_increment"
    template_fillers = {'text': text}
    templates = nlg_object.ans_bert_templates
    curr_templates = templates[state_object.intent]
    template = random.choice(curr_templates)
    return template.format(**template_fillers)


def dialogue_manager(stateObject, stateMachine):
    """
    Method called by the bot.py to retrieve the information to pass to the NLG
    :param stateObject: state object, in which are stores: intent, previous intent, story graph, nodes visited
    :param stateMachine: finate state machine, in which is stored the current state
    :return: string - text
    """
    nlg_model = NLG()
    current_state = stateMachine.state
    if "introduction" in current_state:
        return introduction(stateObject, nlg_model)
    elif "storytelling" in current_state:
        return storytelling(stateObject, nlg_model)
    elif "closing" in current_state:
        return closing(stateObject, nlg_model)
    elif "answering" in current_state:
        return answering(stateObject, nlg_model)
    elif "link_to_survey" in current_state:
        return link_to_survey(stateObject, nlg_model)
    elif "answering_f" in current_state:
        return answering_f(stateObject, nlg_model)
    elif "bert" in current_state:
        answer = ans_bert(stateObject, nlg_model)
        if answer == "next_increment":
            return storytelling(stateObject, nlg_model)
        else:
            return answer

