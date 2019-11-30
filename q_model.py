'''
Q-Learning Policy
'''
import numpy as np

class Policy:
    '''
    Policy class, keeps track of the value of each game state encountered

    States and values are stored in :_policy: as key-value respectively
    '''
    _policy = {}

    def __init__(self, outputs, learning_rate=0.2, discount_factor=0.8):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.default_policy = np.zeros(outputs)

    def update(self, state, next_state, action, reward):
        '''Update the reward estimation for the state'''

        next_reward = self.highest_reward(next_state)
        current_reward = self.highest_reward(state)

        self._policy[state][action] += self.learning_rate * (
            reward + self.discount_factor * (next_reward - current_reward)
        )

    def highest_reward(self, state):
        '''Estimate the highest reward available for the current state'''
        self._policy.setdefault(state, np.copy(self.default_policy))
        return np.max(self._policy[state])

    def get_action_id(self, state):
        '''Pick the action with the highest reward from the current state'''
        max_reward = self.highest_reward(state)
        action_id = np.random.choice(
            np.argwhere(self._policy[state] == max_reward).flatten()
        )

        return action_id
