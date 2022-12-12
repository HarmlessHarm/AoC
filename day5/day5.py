import os
import re
import copy
import numpy as np
from collections import defaultdict

INPUT = "input"
# INPUT = "test"
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)


STACK_9000 = defaultdict(list)


def parseStackLayer(line: str):
    for i, char in enumerate(line):
        if i % 4 != 1:
            continue
        else:
            stackI = i // 4 + 1
            if char.isalpha():
                STACK_9000[stackI].insert(0, char)
            
def parseAction(line: str):
    reg = r'move (?P<N>\d+) from (?P<F>\d+) to (?P<T>\d+)'
    res = re.search(reg, line).groupdict()
    return tuple(map(int, (res["N"], res["F"], res["T"])))

def move9000(N, src, tgt):
    for i in range(N):
        STACK_9000[tgt].append(STACK_9000[src].pop())

def move9001(N, src, tgt):
    toMove = list()
    for i in range(N):
        toMove.append(STACK_9001[src].pop())
    toMove.reverse()
    STACK_9001[tgt] = STACK_9001[tgt] + toMove

with open(IN_PATH, 'r') as file:
    stackPhase = True
    line = None
    while line != "\n":
        line = file.readline()
        parseStackLayer(line)


    STACK_9001 = copy.deepcopy(STACK_9000)
    
    for line in file.readlines():
        result = parseAction(line)
        move9000(*result)
        move9001(*result)
    
    print("puzzle 1: ","".join(list(map(lambda x: STACK_9000[x][-1], sorted(STACK_9000.keys())))))
    print("puzzle 2: ","".join(list(map(lambda x: STACK_9001[x][-1], sorted(STACK_9001.keys())))))
        
    