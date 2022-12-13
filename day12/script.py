import os
import numpy as np
from collections import deque
# import matplotlib.pytplot as plt

INPUT = 'input'
# INPUT = 'test'
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)

def let2num(let: str):
	if let.islower():
		return ord(let) - ord('a') + 1
	if let == 'S':
		return 0
	if let == 'E':
		return 27


def aStar(MAP, start, end):
	pass


def getNeighbours(node, down=False):
	coord = node
	neighbours = list()
	for i,j in [(-1,0), (1,0), (0,-1), (0,1)]:
		newCoord = (coord[0] + i, coord[1] + j)
		if (newCoord[0] < 0 or 
			newCoord[0] > MAP.shape[0] - 1 or 
			newCoord[1] < 0 or 
			newCoord[1] > MAP.shape[1] - 1):
			continue
	
		if (not down and MAP[newCoord] - MAP[coord] <= 1) or (down and MAP[newCoord] - MAP[coord] >= -1):
			newNode = {'coord': newCoord, 'dist': DIST[node] + 1}
			neighbours.append(newNode)

	return neighbours


def dijkstra(start, end):
	finished = False
	unexplored = [start]
	explored = []
	
	d = 0
	maxD = 5000
	while len(unexplored) and not finished and d < maxD:
		toExplore = unexplored.pop(0)
		explored.append(toExplore)
		# DIST[toExplore] = toExplore['dist']

		neighbours = getNeighbours(toExplore, down=True)
		for node in neighbours:
			if node['coord'] not in explored and node['coord'] not in unexplored:
				unexplored.append(node['coord'])
				DIST[node['coord']] = node['dist']
		val = MAP[toExplore]
		if end in unexplored:
			print("Shortest path", DIST[end])
			finished = True
		d += 1
		if d >= maxD-10:
			print("DEPTH OVERFLOW")
		if len(unexplored) < 1:
			# print(DIST)
			printDist()
			print(unexplored)

def downhillClimber(start, end):
	finished = False
	node = start
	while not finished:
		neighbours = getNeighbours(node, down=True)
		best = np.argmin(DIST[neighbours])


def printDist():
	x = '\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in DIST])
	print(x)

with open(IN_PATH, 'r') as file:
	MAP = np.array([list(map(let2num, list(line.strip('\n')))) for line in file.readlines()])

	start = list(zip(*np.where(MAP == 0)))[0]
	end = list(zip(*np.where(MAP == 27)))[0]
	
	DIST = np.ones(MAP.shape, dtype=int) * 1000
	DIST[end] = 0

	dijkstra(end, start)

	print(DIST)
	maxA = min(DIST[np.where(MAP == 1)])
	print(maxA)

