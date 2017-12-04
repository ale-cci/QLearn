# Game Rules:

possible_actions = [0, 1, 2, 3]	# move farmer, cavolo, sheep or wolf
initial_status = [False] * 4

	
def won(status):
	return not (False in status)

def lost(status):
	tmp = [s != status[0] for s in status]
	return tmp[2] and (tmp[1] or tmp[3])

def next_status(status, action):
	tmp = status[:]
	tmp[0] = not tmp[0]
	if action != 0:
		tmp[action] = not tmp[action]
	return tmp