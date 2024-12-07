# https://adventofcode.com/2024/day/1

from collections import Counter

with open("input.txt") as file:
	left_list = []
	right_list = []
	
	for line in file:
		a, b = map(int, line.split())
		left_list.append(a)
		right_list.append(b)
		
	counter = Counter(right_list)
	similarity = sum(n*counter[n] for n in left_list)
	
	print(f"Similarity: {similarity}")

