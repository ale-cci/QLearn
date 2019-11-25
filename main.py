#!/usr/bin/env python3

from problems.labirinth import Game
from q_model import Policy
import numpy as np
import random

def get_reward(game):
    """ Score for the current game state """
    if game.won():
        return 1
    if game.lost():
        return -1
    return -0.2 # negative for finding the fastest solution

game = Game()

# List of possible actions
actions = game.get_actions()

policy = Policy(len(actions))

ATTEMPTS = getattr(game, 'attempts', 100)
for iteration in range(ATTEMPTS):
    game.reset()

    steps = 0
    while not (game.won() or game.lost()):
        steps += 1

        # Taking index of the maximum rewarding action
        state = game.get_state()
        idx = policy.get_action_id(state)


        # Executing the maximum rewarding action
        game.do_action(actions[idx])
        reward = get_reward(game)

        # Updating last performed action policy
        new_state = game.get_state()
        policy.update(state, new_state, idx, reward)


    if game.won():
        print ("Won in ", steps)
    else:
        print ("Lost in ", steps)
