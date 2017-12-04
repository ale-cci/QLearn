# Game Rules:

nof_attempt = 19000

possible_actions = [0, 1, 2, 3, 4, 5, 6, 7]	# place on the X row
initial_status = []	# no queen placed

def _conflict(q1, q2):
	if q1[0] == q2[0]:	# same X coord
		return True
	if q1[1] == q2[1]:	# same Y coord
		return True
	if q1[0] + q1[1] == q2[0] + q2[1]: # same / diagonal
		return True
	if q1[0] - q1[1] == q2[0] - q2[1]: # same \ diagonal
		return True

def won(status):
	return (len(status) == 8) and not lost(status)

def lost(status):
	for i, q1 in enumerate(status):
		for q2 in status[i +1:]:
			if _conflict(q1, q2):
				return True
	return False

def next_status(status, action):
	tmp = status[:]
	tmp.append(((action), len(tmp)))
	return tmp