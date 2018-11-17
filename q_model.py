import numpy as np

class Policy:
    def __init__(self, outputs, λ=0.2, γ=0.8):
        self.λ = λ # learning rate
        self.γ = γ # holding rate
        self.default_policy = np.zeros(outputs)
        self._policy = {}

    def update(self, state, next_state, action, reward):

        next_reward = self.highest_reward(next_state)
        current_reward = self.highest_reward(state)

        self._policy[state][action] += self.λ*(reward + self.γ*(next_reward - current_reward))

    def highest_reward(self, status):
        self._policy.setdefault(status, np.copy(self.default_policy))
        return np.max(self._policy[status])

    def get_action_id(self, status):
        max_reward = self.highest_reward(status)
        return np.random.choice(
                np.argwhere(self._policy[status] == max_reward).flatten()
            )

