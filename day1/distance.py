# https://adventofcode.com/2024/day/1

with open("input.txt") as file:
	left_list = []
	right_list = []
	for line in file:
		(a, b) = map(int, line.split())
		left_list.append(a)
		right_list.append(b)
		
	left_list.sort()
	right_list.sort()
	distances = [abs(a-b) for a, b in zip(left_list, right_list)]
	
	print(f"Distances: {sum(distances)}")

