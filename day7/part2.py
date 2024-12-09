# https://adventofcode.com/2024/day/7 -- Part 2

# This is a really bad solution. For a better solution, see part2_smarter.py

def solution_exists(total, operands):
	p = my_range(0, 3**(len(operands)-1), 3) 
	num_operators = len(operands)-1
	for i in p:
		digits = len(i)
		if digits < num_operators:
			i = "0"*(num_operators-digits)+i
		ans = evaluate(operands.copy(), i)
		# print(f"{i}: {ans}")
		if total == ans:
			return True
	return False

			
def my_range(start,end,base,step=1):
	def Convert(n,base):
		string = "0123456789ABCDEF"
		if n < base:
			return string[n]
		else:
			return Convert(n//base,base) + string[n%base]
	return (Convert(i,base) for i in range(start,end,step))
									
def evaluate(operands, v):
	# print(f"operands: {operands}, v: {v}")
	total = 0
	for i in range(len(operands)-1):
		if v[i] == '0':
			operands[i+1] = operands[i] + operands[i+1]
		elif v[i] == '1':
			operands[i+1] = operands[i] * operands[i+1]
		else:
			operands[i+1] = int(str(operands[i]) + str(operands[i+1]))
		
	return operands[-1]		
		
with open("test.txt") as file:
	total = 0	
	for line in file:
		parts = line.strip().split(':')
		goal = int(parts[0])
		operands = list(map(int, parts[1].strip().split()))
		found_solution = solution_exists(goal, operands)
		if found_solution:
			total += goal
		# print(f"total: {total}, operands: {operands}, good: {good}")
	print(total)


