import os

INPUT = "input"
# INPUT = "test"
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)

def splitRucksack(input_str):
	half = len(input_str)//2
	left = input_str[:half]
	right = input_str[half:]
	return set(left), set(right)

def intersection(left, right):
	inter = left.intersection(right)
	if len(inter) == 1:
		return str(list(inter)[0])

def trioIntersection(one, two, three):
	inter = one & two & three
	return str(list(inter)[0])

def prioScore(char):
	if char.islower():
		return ord(char) - ord('a') + 1
	return ord(char) - ord('A') + 27

def puzzle1Score(line):
	left, right = splitRucksack(line)
	inter = intersection(left, right)
	return prioScore(inter)

def puzzle2Score(chunk):
	one, two, three = list(map(set, chunk))
	inter = trioIntersection(one, two, three)
	return prioScore(inter)

with open (IN_PATH, 'r') as file:
	all_lines = [line.strip('\n') for line in file.readlines()]
	score1 = sum(map(puzzle1Score, all_lines))

	chunks = [all_lines[i:i+3] for i in range(0, len(all_lines), 3)]
	score2 = sum(map(puzzle2Score, chunks))
		
	print("puzzle 1", score1)
	print("puzzle 2", score2)
