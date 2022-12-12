import os
from itertools import islice

INPUT = "input"
# INPUT = "test"
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)


def window(iterable, size=2):
    it = iter(iterable)
    window = tuple(islice(it, size))
    if len(window) == size:
        yield window

    for e in it:
        window = window[1:] + (e, )
        yield window

with open(IN_PATH, 'r') as file:
    line = file.readline()

for i, win in enumerate(window(line, 4), 4):
    if len(set(win)) == len(win):
        print(i, win)
        break

for i, win in enumerate(window(line, 14), 14):
    if len(set(win)) == len(win):
        print(i, win)
        break