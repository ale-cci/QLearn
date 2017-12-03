import random
T = 1 # target, goal
E = 2 # error, pit

alpha = 0.2
gamma = 0.8

ground = [[0, 0, 0, 0, 0, T],
		  [0, 0, 0, 0, 0, E],
		  [0, 0, 0, 0, 0, 0]]
# possible actions top, down, left, right
actions = [(0,-1), (0, 1), (-1, 0), (1, 0)]

# start player coord
start = (0, 2)
def_list = [0, 0, 0, 0]
def move(coord, d):
	x, y = coord
	dx, dy = d
	x0 = x + dx
	y0 = y + dy
	if x0 < 0 or x0 >= len(ground[0]):
		x0 = x
	if y0 < 0 or y0 >= len(ground):
		y0 = y
	return x0, y0

# Map the player position and the list of next rewardings
Q = {}
NOF_GAMES = 60
for i in range(NOF_GAMES):
	coord = start
	iters = 0
	Q.setdefault(str(coord), def_list[:])	# set default 
	while True:
		iters += 1
		# moving char
		m = max(Q[str(coord)])	# max reward
		d = random.choice([i for i, j in enumerate(Q[str(coord)]) if j == m])	# random choice a directoin from the highest reward dirs

		last_coord = coord # save last dir before moving
		coord = move(coord, actions[d])	# move 

		# calculating reward

		under = ground[coord[1]][coord[0]]

		if under == 0:
			reward = -0.2
		elif under == T:
			reward = +1
		elif under == E:
			reward = -1

		# updating Q value
		Q.setdefault(str(coord), def_list[:])	# set defaults for new status
		# updating policy
		#print(last_coord, d, Q[str(last_coord)], alpha*(reward + gamma*max(Q[str(coord)])-Q[str(last_coord)][d]))
		Q[str(last_coord)][d] += alpha*(reward + gamma*max(Q[str(coord)])-Q[str(last_coord)][d])

		#print (last_coord, Q[str(last_coord)], d)
		if under == T or under == E:
			break
	print (iters)

for i, k in Q.items():
	print(i, k)