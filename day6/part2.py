# https://adventofcode.com/2024/day/6 -- Part 2

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
	
def patrol_is_loop(map, guard_position, guard_direction):
	'''
	Returns True if the resulting patrol for map, guard_position, guard_direction
	results in a loop. Returns False otherwise.
	'''
	# A vector is a (position, direction) tuple.
	# visited_vectors records the set of positions the guard has visited
	# along with the direction the guard was facing in the position.
	# If the guard visits the same position facing the same direction,
	# more than once then we known the guard is in a loop.
	visited_vectors = set((guard_position, guard_direction)) 
	is_loop = False
	while True:
		next_position = add_tup(guard_position, guard_direction)
		if next_position in map:
			if map[next_position] == '.':
				guard_position = next_position
				if (guard_position, guard_direction) in visited_vectors:
					is_loop = True
					break
				visited_vectors.add((guard_position, guard_direction))
			else:
				guard_direction = RIGHT_TURNS[guard_direction]
				if (guard_position, guard_direction) in visited_vectors:
					is_loop = True
					break
				visited_vectors.add((guard_position, guard_direction))
		else:
			break
				
	return is_loop

(map, guard_position, guard_direction) = read_map("input.txt")
visited_positions = patrol(map, guard_position, guard_direction)

original_guard_position = guard_position
original_guard_direction = guard_direction

# try putting an obstacle in each visited position, then see if guard
# exits or is stuck in a loop

visited_positions.remove(original_guard_position)
loop_count = 0

for obstacle_position in visited_positions:
	map[obstacle_position] = '#'
	loop_count += patrol_is_loop(map, original_guard_position, original_guard_direction)
	map[obstacle_position] = '.'
		
print(f"Loops: {loop_count}")
