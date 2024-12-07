# https://adventofcode.com/2024/day/1

with open("input.txt") as file:
	left_list = []
	right_list = []
	for line in file:
		p = list(map(int, line.split()))
		left_list.append(p[0])
		right_list.append(p[1])
		
	left_list.sort()
	right_list.sort()
	pairs = zip(left_list, right_list)
	distances = [abs(p[0]-p[1]) for p in pairs]
	
	print(f"Distances: {sum(distances)}")

