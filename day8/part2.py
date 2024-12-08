# https://adventofcode.com/2024/day/8 -- Part 2

'''
Same as the solution to Part 1. We just need to update get_antinodes()
'''

import itertools

def read_file(filename):
	'''
	Returns a tuple (antennas, grid) where...
	
	antennas is a dict whose keys are the frequency identifiers (a-z, A-Z, 0-9)
	and whose values are a list of (row, column) tuples indicating the
	position of the antennas of that frequency in the grid.
	
	e.g. {'0': [(1, 8), (2, 5), (3, 7), (4, 4)], 'A': [(5, 6), (8, 8), (9, 9)]}
	
	grid is a dict whose keys are (row, column) tuples and whose value
	is the character in the grid (either '.' or one of frequency characters)
	
	e.g. {(0, 0): '.', (0, 1): '.', (0, 2): '.', ... }
	'''
	with open(filename) as file:
		grid = {}
		antennas = {}
		for row, line in enumerate(file):
			for col, value in enumerate(line.strip()):
				if value != '.':
					if value in antennas:
						l = antennas[value]
						l.append((row, col))
					else:
						antennas[value] = [(row, col)]
				grid[(row, col)] = value
		return (antennas, grid)
				
def get_antinodes(c1, c2, grid):
	'''
	c1 and c2 are the coords of a pair of antennae.
	grid is a dictionary whose keys are (row, column) tuples in the grid.	
	Returns the list of coords for the antinodes of that pair of antennae.
	'''
	delta = (c1[0]-c2[0], c1[1]-c2[1])	
	
	antinodes = []					# list of antinodes to return
	recipes = [(c1, 1), (c2, -1)] 	# incrementally add delta to c1
									# incrementally subtract delta from c2
	
	for coord, step in recipes:
		i = 0 						# starting at 0 includes the antenna position
		while True:
			antinode = (coord[0]+delta[0]*i, coord[1]+delta[1]*i)
			if antinode in grid:
				antinodes.append(antinode)
				i += step
			else:
				break				# gone off the edge of the grid
	
	return antinodes
									
(ant, grid) = read_file("input.txt")
antinodes = set()

for freq, positions in ant.items():
	for p in itertools.combinations(positions, 2):
		antinodes.update(get_antinodes(*p, grid))

print(f"Number of antinodes: {len(antinodes)}")
