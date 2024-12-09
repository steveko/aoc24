# https://adventofcode.com/2024/day/8 -- Part 2

'''
Same as the solution to Part 1. We just need to update get_antinodes()
'''

import itertools

def read_file(filename):
	'''
	Returns a 3-tuple (antennas, row_count, column_count) where...
	
	antennas is a dict whose keys are the frequency identifiers (a-z, A-Z, 0-9)
	and whose values are a list of (row, column) tuples indicating the
	position of the antennas of that frequency in the grid.
	
	e.g. {'0': [(1, 8), (2, 5), (3, 7), (4, 4)], 'A': [(5, 6), (8, 8), (9, 9)]}
	
	row_count is the number of rows in the grid.
	column_count is the number of columns in the grid.
	'''
	with open(filename) as file:
		antennas = {}
		row_count = 0
		for row, line in enumerate(file):
			row_count += 1
			column_count = 0
			for col, value in enumerate(line.strip()):
				column_count += 1
				if value != '.':
					if value in antennas:
						antennas[value].append((row, col))
					else:
						antennas[value] = [(row, col)]
		return (antennas, row_count, column_count)
		
def is_valid(coord, row_count, column_count):
	r, c = coord
	return all([r >= 0, c >= 0, r < row_count, c < column_count])
										
def get_antinodes(antenna1, antenna2, row_count, column_count):
	'''
	antenna1 and antenna2 are the coords of two antennas.
	row_count and column_count reflect the size of the grid.
	Returns the list of coords for the antinodes of antenna1 and antenna2
	'''
	row1, column1 = antenna1
	row2, column2 = antenna2
	delta_row, delta_column = (row1 - row2, column1 - column2)
	
	antinodes = []					# list of antinodes to return
	
	recipes = [(antenna1, 1), (antenna2, -1)] 
									# incrementally add delta to c1
									# incrementally subtract delta from c2
	
	for antenna, step in recipes:
		i = 0 						# starting at 0 includes the antenna position
		row, column = antenna
		while True:
			antinode = (row + delta_row*i, column + delta_column*i)
			if is_valid(antinode, row_count, column_count):
				antinodes.append(antinode)
				i += step
			else:
				break				# gone off the edge of the grid
	
	return antinodes
									
(antennas, row_count, column_count) = read_file("input.txt")
antinodes = set()

for freq, positions in antennas.items():
	for pair_of_antennas in itertools.combinations(positions, 2):
		antinodes.update(get_antinodes(*pair_of_antennas, row_count, column_count))

print(f"Number of antinodes: {len(antinodes)}")
