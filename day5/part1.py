# https://adventofcode.com/2024/day/5 -- Part 1

rules = []
updates = []
		
with open("test.txt") as file:
	for line in file:
		if '|' in line:
			p = list(map(int, line.strip().split('|')))
			rules.append(p)
		elif ',' in line:
			p = list(map(int, line.strip().split(',')))
			updates.append(p)

middle_sum = 0

for update in updates:
	# create mapping from a number in update to its index in update
	index_of = {}
	for i, n in enumerate(update):
		index_of[n] = i
	
	correct = True
	for left, right in rules:
		if left in index_of and right in index_of:
			if index_of[left] > index_of[right]:
				correct = False
				break
	
	if correct:
		middle_sum += update[int(len(update)/2)]
		
print(middle_sum)
