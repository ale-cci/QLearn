#!/usr/bin/env python

from PROBLEMS.caprecavoly import  Game
import numpy as np
import random

def get_reward(game):
    """ Score for the current game status """
    if game.won():
        return 1
    if game.lost():
        return -1
    return -0.2 # negative for finding the fastest solution

Q = {} # Policy

λ = 0.2 # learning rate
γ = 0.8 # holding rate

game = Game()
ATTEMPTS = getattr(game, 'attempts', 100)

# List of possible actions
actions = game.get_actions()

for iteration in range(ATTEMPTS):
    game.reset()

    if iteration == 0:
        # Setting default policy for the starting status
        Q[game.get_status()] = np.zeros(len(actions))

    steps = 0
    while not (game.won() or game.lost()):
        steps += 1

        # Taking index of the maximum rewarding action
        status = game.get_status()
        idx = np.random.choice(np.argwhere(Q[status] == np.amax(Q[status])).flatten())

        # Executing the maximum rewarding action
        game.do_action(actions[idx])
        reward = get_reward(game)

        # Updating last performed action policy
        new_status = game.get_status()
        Q.setdefault(new_status, np.ones(len(actions))/len(actions))
        Q[status][idx] += λ*(reward + γ*(np.max(Q[new_status])-Q[status][idx]))


    if game.won():
        print ("Won in ", steps)
    else:
        print ("Lost in ", steps)
