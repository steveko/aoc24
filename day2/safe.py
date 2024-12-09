# https://adventofcode.com/2024/day/2

def is_safe(levels):
	deltas = [levels[i]-levels[i-1] for i in range(1,len(levels))]
	first_check = deltas[0] > 0
	return all(1 <= abs(d) <= 3 for d in deltas) and all((d > 0) == first_check for d in deltas[1:])
	
with open("input.txt") as file:
	rows = [list(map(int, line.split())) for line in file]
	print(f"Safe: {sum(is_safe(r) for r in rows)}")

