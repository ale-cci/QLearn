import numpy as np

class Policy:
    _policy = {}

    def __init__(self, outputs, learning_rate=0.2, discount_factor=0.8):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.default_policy = np.zeros(outputs)

    def update(self, state, next_state, action, reward):

        next_reward = self.highest_reward(next_state)
        current_reward = self.highest_reward(state)

        self._policy[state][action] += self.learning_rate * (
                reward + self.discount_factor * (next_reward - current_reward)
            )

    def highest_reward(self, status):
        self._policy.setdefault(status, np.copy(self.default_policy))
        return np.max(self._policy[status])

    def get_action_id(self, status):
        max_reward = self.highest_reward(status)
        action_id = np.random.choice(
                np.argwhere(self._policy[status] == max_reward).flatten()
                )

        return action_id
