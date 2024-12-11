N = (-1, 0)
S = (1, 0)
E = (0, 1)
W = (0, -1)
DIRECTIONS = [N, S, E, W]

def read_file(filename):
	with open(filename) as file:
		trailheads = []
		grid = {}
		for row, line in enumerate(file):
			for col, value in enumerate(line.strip()):
				grid[(row, col)] = int(value)
				if value == '0':
					trailheads.append((row, col))
		return grid, trailheads
		
def add_locs(a, b):
	ar, ac = a
	br, bc = b
	return (ar+br, ac+bc)

def reachable_peaks(grid, start_loc):
	# find N, S, E, W next step positions
	peaks = set()
	start_alt = grid[start_loc]
	for d in DIRECTIONS:
		step_loc = add_locs(start_loc, d)
		if step_loc in grid:
			step_alt = grid[step_loc]
			if step_alt == start_alt+1:
				if step_alt == 9:
					peaks.add(step_loc)
				else:
					peaks.update(reachable_peaks(grid, step_loc))
	
	return peaks
	
def valid_trails(grid, start_loc):
	'''
	Returns a list of valid trails in grid starting at start_loc.
	A trail is a list of locs represent the path of a trail.
	'''
	subtrails = []
	start_alt = grid[start_loc]
	for d in DIRECTIONS:
		step_loc = add_locs(start_loc, d)
		if step_loc in grid:
			step_alt = grid[step_loc]
			if step_alt == start_alt+1:
				if step_alt == 9:
					subtrails.append([step_loc])
				else:
					subtrails += valid_trails(grid, step_loc)
	
	full_trails = [[start_loc] + subtrail for subtrail in subtrails]
	
	return full_trails		

def sum_scores(grid, trailheads):
	ans = 0
	for trailhead in trailheads:
		ans += len(reachable_peaks(grid, trailhead))
	return ans
	
def sum_rankings(grid, trailheads):
	ans = 0
	for trailhead in trailheads:
		ans += len(valid_trails(grid, trailhead))
	return ans

grid, trailheads = read_file("input.txt")

print(sum_rankings(grid, trailheads))
