# https://adventofcode.com/2024/day/3 -- Part 2

import re

with open("input.txt") as file:
	total = 0
	enabled = True
	pattern = r'mul\((\d+),(\d+)\)|(do\(\))|(don\'t\(\))'
	for (x, y, enable, disable) in re.findall(pattern, file.read()):
		if enable:
			enabled = True
		elif disable:
			enabled = False
		elif enabled:
			total += int(x)*int(y)
	print(total)

