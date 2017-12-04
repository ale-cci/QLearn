import queens as game
import random

# Defining normal functions
def finished(status):
	return game.won(status) or game.lost(status)

def get_reward(status):
	if game.won(status):
		return 1
	if game.lost(status):
		return -1
	return -0.2

nof_actions = len(game.possible_actions)
default_choices = [0] * nof_actions

Q = {}
Q[str(game.initial_status)] = default_choices
alpha = 0.2	# learning rate
gamma = 0.8 # holding rate

try:
	GAMES = game.nof_attempt
except:
	GAMES = 100

for _ in range(GAMES):
	status = game.initial_status
	iterations = 0

	while not finished(status):
		iterations += 1
		max_value = max(Q[str(status)])
		action = random.choice([i for i, j in enumerate(Q[str(status)]) if j == max_value])	# retrieve the most rewarding action

		# do the best move
		last_status = status
		status = game.next_status(action=action, status=status)
		reward = get_reward(status);

		Q.setdefault(str(status), default_choices[:])
		Q[str(last_status)][action] += alpha * (reward + gamma*max(Q[str(status)]) - Q[str(last_status)][action])

	if game.won(status):
		print ("won in ", iterations)
	else:
		print ("Lost in ", iterations) 