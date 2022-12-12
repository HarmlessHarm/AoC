import os
import re
import numpy as np


INPUT = "input"
# INPUT = "test"
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)


def extractRanges(line):
    reg = r"(?P<from1>\d+)-(?P<to1>\d+),(?P<from2>\d+)-(?P<to2>\d+)"
    groups = re.search(reg, line).groupdict()
    range_1 = np.arange(int(groups['from1']), int(groups['to1'])+1)
    range_2 = np.arange(int(groups['from2']), int(groups['to2'])+1)
    return (range_1, range_2)

def completelyOverlaps(range_pair):
    range_1, range_2 = range_pair
    intersect = set(range_1) & set(range_2)

    return len(intersect) == len(range_1) or len(intersect) == len(range_2)

def overlaps(range_pair):
    range_1, range_2 = range_pair
    intersect = set(range_1) & set(range_2)
    return len(intersect) > 0
    

with open(IN_PATH, 'r') as file:
    all_lines = [line.strip('\n') for line in file.readlines()]
    parsed_ranges = list(map(extractRanges, all_lines))
    ranges_overlap_completely = list(map(completelyOverlaps, parsed_ranges))
    print("puzzle 1:", sum(ranges_overlap_completely))
    ranges_overlap = list(map(overlaps, parsed_ranges))
    print("puzzle 2:", sum(ranges_overlap))
