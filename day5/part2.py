# https://adventofcode.com/2024/day/5 -- Part 2

def index_map(update):
	index_of = {}
	for i, n in enumerate(update):
		index_of[n] = i
	return index_of

def apply_rules(update, rules):
	index_of = index_map(update)
	corrected = False	
	for left, right in rules:
		if left in index_of and right in index_of:
			if index_of[left] > index_of[right]:
				corrected = True
				update[index_of[left]] = right
				update[index_of[right]] = left
				index_of[left], index_of[right] = index_of[right], index_of[left]
	return corrected

# Read input file, populate rules and updates lists	
rules = []
updates = []
with open("input.txt") as file:
	for line in file:
		if '|' in line:
			p = list(map(int, line.strip().split('|')))
			rules.append(p)
		elif ',' in line:
			p = list(map(int, line.strip().split(',')))
			updates.append(p)

# Find the wrong updates
wrong_updates = []
for update in updates:
	index_of = index_map(update)
	for left, right in rules:
		if left in index_of and right in index_of:
			if index_of[left] > index_of[right]:
				wrong_updates.append(update)
				break		
		
# Correct the wrong updates and sum up middle numbers
middle_sum = 0
for update in wrong_updates:
	corrected = True
	while corrected:
		corrected = apply_rules(update, rules)
	middle_sum += update[int(len(update)/2)]
		
print(middle_sum)


