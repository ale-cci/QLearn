# Game Rules:
possible_actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]	# Top Down Left Right
initial_status = (0, 0)			# Start position

_hidden_obstacles = [
]

_game_w = 5
_game_h = 5

def won(status):
	return status == (_game_w, _game_h)

def lost(status):
	return status in _hidden_obstacles

def next_status(status, action):
	dx, dy = possible_actions[action]
	x, y = status

	# Bounding new Coords
	x0 = min(max(0, x+dx), _game_w)
	y0 = min(max(0, y+dy), _game_h)
	return x0, y0