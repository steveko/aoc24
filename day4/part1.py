# https://adventofcode.com/2024/day/4 -- Part 1

import re

def check_deltas(x, y, puzzle, deltas):
	"""
	deltas is a list of 3-tuples of the form (dx, dy, letter).
	Returns true if the letter of puzzle at the dx, dy offsets
	from x, y match letter for every 3-tuple in the list.
	"""
	return all(puzzle[y+dy][x+dx] == letter for dx, dy, letter in deltas)

def count_down_diag_xmas_at(x, y, puzzle):
	"""
	Assume puzzle[y][x] == 'X'
	Checks for XMAS starting at x, y and going downward diagonally in
	either direction. Returns total number of XMAS instances found.
	"""
	deltas_right = [(1, 1, 'M'), (2, 2, 'A'), (3, 3, 'S')]
	deltas_left = [(-1, 1, 'M'), (-2, 2, 'A'), (-3, 3, 'S')]
	
	puzzle_width = len(puzzle[0])
	
	# only check deltas_right if x is not too near right edge
	count = (x <= puzzle_width - 4) and check_deltas(x, y, puzzle, deltas_right)
	
	# only check deltas_left if x is not too near the left edge
	count += (x >= 3) and check_deltas(x, y, puzzle, deltas_left)
			
	return count
	
def count_xmas_in_line(line):
	return len(re.findall(r'XMAS', line)) + len(re.findall(r'SAMX', line))
	
def count_down_diag_xmas_in_puzzle(puzzle):
	count = 0
	for y, line in enumerate(puzzle[:-3]):
		for x in [m.start() for m in re.finditer(r'X', line)]:
			count += count_down_diag_xmas_at(x, y, puzzle)				
	return count
		
def rotated_puzzle(puzzle):
	rotated = ["" for x in range(len(puzzle[0]))]
	for line in puzzle:
		for x, c in enumerate(line):
			rotated[x] += c	
	return rotated
		
with open("input.txt") as file:
	puzzle = []
	for line in file:
		puzzle.append(line)

	count = 0
							
	# Count all horizontal instances in each line
	for line in puzzle:
		count += count_xmas_in_line(line)

	# Count all vertical instances by counting all horizontal instances in each
	# line of rotated puzzle
	for line in rotated_puzzle(puzzle):
		count += count_xmas_in_line(line)
			
	# Count all downward diagonal instances
	count += count_down_diag_xmas_in_puzzle(puzzle)
	
	# Count all upward diagonal instances by counting all downward diagonal
	# instances in the vertically flipped puzzle
	puzzle.reverse()
	count += count_down_diag_xmas_in_puzzle(puzzle)
	
	print(f"Total: {count}")
	

