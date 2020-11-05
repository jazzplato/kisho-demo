#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from utils import constants


class KishoStateTransition:
    def __init__(self, name, counter=1, prob=0):
        self.name = name
        self.counter = counter
        self.prob = 0


class KishoState:
    def __init__(self, name, level=0):
        self.name = name
        self.level = level
        self.transitions = {}
        self.counter = 0

    def add_transition(self, state_name):
        transition = KishoStateTransition(state_name)
        self.transitions[state_name] = transition
        self.counter += transition.counter

    def update_transition_probs(self, curr_state_name=None):
        # update the current state
        if curr_state_name and curr_state_name in self.states:
            self.states[curr_state_name].counter += 1
            self.counter += 1
        # re-calculate the probs for each of the transitions
        for transition in self.transitions.values():
            transition.prob = transition.counter / self.counter


class KishoModel:
    def __init__(self,
                 name,
                 curr_state_name,
                 prediction_cycle=constants.DEFAULT_PREDICTION_CYCLE):
        self.name = name
        self.curr_state_name = curr_state_name
        self.states = {}
        self.history_states = [curr_state_name]
        self.prediction_cycle = prediction_cycle
        # self.history_size = 100

    def add_state(self, state):
        self.states[state.name] = state

    def update_model(self, curr_state_name):
        last_state = self.states[self.history_states[-1]]
        last_state.update_transition_probs(curr_state_name)


def init_system_model(raw_system_states):
    system_model = KishoModel(raw_system_states.name,
                              raw_system_states.curr_state_name,
                              raw_system_states.prediction_cycle)
    for raw_state in raw_system_states.states:
        curr_state = KishoState(raw_state.name, raw_state.level)
        for transition in raw_state.transitions:
            curr_state.add_transition(transition.name)
        curr_state.update_transition_probs()
        system_model.add_state(curr_state)
    return system_model