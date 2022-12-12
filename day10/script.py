import os
import numpy as np

INPUT = 'input'
# INPUT = 'test'
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)

REG_HIST = list()
REG_X = 1

def parseLine(line):
	if "noop" in line:
		return 0, 1
	add = int(line.strip('\n').split(' ')[-1])
	return add, 2

def calcSignal(T):
	return T * REG_HIST[T-1]


with open(IN_PATH, 'r') as file:
	for line in file.readlines():
		add, time = parseLine(line)
		for t in range(time):
			REG_HIST.append(REG_X)
		REG_X += add

checks = list(range(20, 240, 40))

print(sum(map(calcSignal, checks)))

# import matplotlib.pyplot as plt

# plt.plot(REG_HIST)
# plt.show()


def printScreen(screen):
	x = '\n'.join([''.join(['#' if item else '.' for item in row]) for row in screen])
	print(x)

SCREEN = np.zeros((240//40, 40))
printScreen(SCREEN)
	

for i, reg in enumerate(REG_HIST):
	lineNr = i // 40
	pixelNr = i % 40
	print(i, reg)
	if reg >= pixelNr - 1 and reg<= pixelNr + 1:
		SCREEN[lineNr, pixelNr] = 1

printScreen(SCREEN)
