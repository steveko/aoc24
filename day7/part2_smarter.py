# https://adventofcode.com/2024/day/7 -- Parts 1 & 2

def solution_exists(goal, operands, operations):
	"""
	Recursive approach... e.g. f(7290, [6 8 6 15]) is equivalent to:
		
		f(7290, [6+8 6 15]) ||
		f(7290, [6*8 6 15]) ||
		f(7290, [6||8 6 15])
		
	if first part is > goal, then no need to check that branch any further
	because all operands are positive.
	"""
	
	# We should never hit case where number of operands is < 2
	(a, b) = operands[:2]
	
	# Base case
	if len(operands) == 2:
		return any(goal == f(a, b) for f in operations)
	
	# Recursive case
	for f in operations:
		ans = f(a, b)
		if goal >= ans and solution_exists(goal, [ans] + operands[2:], operations):
			return True
			
	return False

OPS_PART_1 = [
	lambda a, b: a+b,
	lambda a, b: a*b
	]

OPS_PART_2 = [
	lambda a, b: a+b,
	lambda a, b: a*b,
	lambda a, b: int(str(a)+str(b))
	]

with open("test.txt") as file:
	total = 0	
	for line in file:
		parts = line.strip().split(':')
		goal = int(parts[0])
		operands = list(map(int, parts[1].strip().split()))
		found_solution = solution_exists(goal, operands, OPS_PART_2)
		if found_solution:
			total += goal
		print(f"goal: {goal}, operands: {operands}, found solution: {found_solution}")
	print(total)
