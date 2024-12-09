# https://adventofcode.com/2024/day/7 -- Part 1

# This is a really bad solution. For a better solution, see part2_smarter.py

def is_valid(total, operands):
	for i in range(2**(len(operands)-1)):
		ans = evaluate(operands.copy(), i)
		# print(f"{i}: {ans}")
		if total == ans:
			return True
	return False

				
def evaluate(operands, v):
	bit_to_operator = ["+", "*"]
	operators = []
	total = 0
	for i in range(len(operands)-1):
		if v & 1 == 0:
			operands[i+1] = operands[i] + operands[i+1]
		else:
			operands[i+1] = operands[i] * operands[i+1]
		v = v >> 1
		
	return operands[-1]		
		

with open("input.txt") as file:
	ans = 0	
	for line in file:
		parts = line.strip().split(':')
		total = int(parts[0])
		operands = list(map(int, parts[1].strip().split()))
		good = is_valid(total, operands)
		if good:
			ans += total
		# print(f"total: {total}, operands: {operands}, good: {good}")
	print(ans)



