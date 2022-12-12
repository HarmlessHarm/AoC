import os
import numpy as np
import math

INPUT = 'input'
# INPUT = 'test'
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)

TAIL_HIST = set()


def stepHead(dir, pos):
	if dir == "R":
		pos[0] += 1
	elif dir == "L":
		pos[0] -= 1
	elif dir == "U":
		pos[1] += 1
	elif dir == "D":
		pos[1] -= 1
	# print(pos)
	return pos

def getDistAndDir(head, tail):
	dX = head[0] - tail[0]
	dY = head[1] - tail[1]
	return math.sqrt(dX ** 2 + dY **2), (min(abs(dX), 1)*np.sign(dX), min(abs(dY), 1)*np.sign(dY))

def stepTail(tail, head):
	dist, dir = getDistAndDir(head, tail)
	if (dist - 1) >= 1:
		tail[0] += dir[0]
		tail[1] += dir[1]
	return tail

def visualize(head, tail):
	GRID = np.zeros((6,6))
	hx, hy = head
	tx, ty = tail
	GRID[hx, hy] = 1
	GRID[tx, ty] = 2
	print(GRID)
	
def visualizeTail():
	GRID = np.zeros((6,5))
	for x, y in TAIL_HIST:
		GRID[x, y] = 1
	print(GRID)

def parseLine(line):
	[dir, n] = line.strip('\n').split(' ')
	return (dir, int(n))

with open(IN_PATH, 'r') as file:
	head = [0,0]
	# tail = [0,0]
	tails = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
	TAIL_HIST.add(tuple(tails[-1]))
	for line in  file.readlines():
		dir, nSteps = parseLine(line)
		for n in range(nSteps):
			head = stepHead(dir, head)
			prevKnot = head
			for tail in tails:
				tail = stepTail(tail, prevKnot)
				prevKnot = tail
			TAIL_HIST.add(tuple(tail))

print(len(TAIL_HIST))

	
