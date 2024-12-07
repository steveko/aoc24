# https://adventofcode.com/2024/day/3 -- Part 1

import re

with open("input.txt") as file:
	total = 0
	for x, y in re.findall(r'mul\((\d+),(\d+)\)', file.read()):
		total += int(x)*int(y)
	print(total)

