import os
import re

INPUT = "input"
INPUT = "test"
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)

def contains(line):
	print("CONTAINS")
	reg = r"(?P<from1>\d+)-(?P<to1>\d+),(?P<from2>\d+)-(?P<to2>\d+)"
	result = re.search(reg, line).groupdict()
	range1 = np.arange(int(result['from1']), int(result['to1']))
	range2 = np.arange(int(result['from2']), int(result['to2']))
	print(range1, range2)
	
	return False


with open(IN_PATH, 'r') as file:
	all_lines = [line for line in file.readlines()]
	
	print(sum(list(map(contains, all_lines))))