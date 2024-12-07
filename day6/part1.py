# https://adventofcode.com/2024/day/6 -- Part 1

# Directions: (delta_row, delta_column) tuples
N = (-1, 0)
S = (1, 0)
W = (0, -1)
E = (0, 1)

# Makes it easy to determine next direction turning right
RIGHT_TURNS = { N: E, E: S, S: W, W: N }

def read_map(filename):
	'''
	Returns 3-tuple: (map, guard_position, guard_direction)
	
	- map is a dictionary whose keys are (row, column) tuples and whose
	  values are the content at that position on the map ('.' or '#').
	  
	- guard_position is a (row, column) tuple.
	
	- guard_direction is a (delta_row, delta_column) tuple (N, S, W, or E).
	'''
	with open(filename) as file:
		map = {}
		for row, line in enumerate(file):
			for col, value in enumerate(line.strip()):
				if value == '^':
					# Capture the guard position, and make sure to record this
					# as an empty space in the map
					guard_position = (row, col)
					value = '.'
				map[(row, col)] = value
		return (map, guard_position, N)

def add_tup(a, b):
	'''
	Add two 2-tuples together element-wise.
	'''
	return (a[0]+b[0], a[1]+b[1])

def patrol(map, guard_position, guard_direction):
	'''
	Returns a set of (row, column) tuples which represent all the visited
	positions by the guard.
	'''
	visited_positions = set()
	visited_positions.add(guard_position)	
	while True:
		next_position = add_tup(guard_position, guard_direction)
		if next_position in map:
			if map[next_position] == '.':
				guard_position = next_position
				visited_positions.add(next_position)
			else:
				guard_direction = RIGHT_TURNS[guard_direction]
		else:
			break
	return visited_positions
	
(map, guard_position, guard_direction) = read_map("test.txt")
visited_positions = patrol(map, guard_position, guard_direction)

print(f"Visited positions: {len(visited_positions)}")
