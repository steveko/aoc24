# https://adventofcode.com/2024/day/4 -- Part 2

import re

def is_xmas(x, y, puzzle):
	upper_left = puzzle[y-1][x-1]
	upper_right = puzzle[y+1][x-1]
	bottom_left = puzzle[y-1][x+1]
	bottom_right = puzzle[y+1][x+1]
	
	first_check = (upper_left == 'S' and bottom_right == 'M') or (upper_left == 'M' and bottom_right == 'S')
	second_check = (upper_right == 'S' and bottom_left == 'M') or (upper_right == 'M' and bottom_left == 'S')
	
	return first_check and second_check
	
		
with open("input.txt") as file:
	puzzle = []
	for line in file:
		puzzle.append(line)
			
	count = 0
	
	# Find all instances of A that are not in the first or last rows or columns
	for y, line in enumerate(puzzle[1:-1]):
		x_positions = [m.start() for m in re.finditer(r'A', line[:-1])]
		for x in x_positions:
			if x > 0:
				count += is_xmas(x, y+1, puzzle)
				
	print(f"Count: {count}")
	
