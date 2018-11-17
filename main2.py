from PROBLEMS.labirinth import  Game
import numpy as np
import random

# Defining normal functions
def finished(status):
    return game.won(status) or game.lost(status)

def get_reward(game):
    if game.won():
        return 1
    if game.lost():
        return -1
    return -0.2

Q = {}

λ = 0.2	# learning rate
γ = 0.8 # holding rate


ATTEMPTS = 30
game = Game()
for iteration in range(ATTEMPTS):
    game.reset()
    if iteration == 0:
        Q[game.encoded_status()] = np.zeros(len(game.get_actions()))

    steps = 0
    while not (game.won() or game.lost()):
        steps += 1
        status = game.encoded_status()
        actions = game.get_actions()
        maxes = np.argwhere(Q[status] == np.amax(Q[status])).flatten()
        idx = np.random.choice(maxes)


        
        game.do_action(actions[idx])
        reward = get_reward(game)

        new_status = game.encoded_status()
        Q.setdefault(new_status, np.ones(len(actions))/len(actions))
        Q[status][idx] += λ*(reward + γ*(np.max(Q[new_status])-Q[status][idx]))


    if game.won():
        print ("won in ", steps)
    else:
        print ("Lost in ", steps)
