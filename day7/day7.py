import os
import re
from functools import reduce
import operator

INPUT = "input"
INPUT = "test2"
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)


FS = {'/' : {}}
CWD = FS
CRUMBLE = list()
DIR_PATHS = set()


def get_by_path(root, items):
    return reduce(operator.getitem, items, root)

def set_by_path(root, items, value):
    get_by_path(root, items[:-1])[items[-1]] = value

def parse_line(line):
    global FS, CWD, CRUMBLE

    if line[:4] == '$ cd':
        tgt = line[5:]
        if tgt == '..':
            CRUMBLE.pop()
        else:
            CRUMBLE.append(tgt)
            DIR_PATHS.add(tuple(CRUMBLE))

        CWD = get_by_path(FS, CRUMBLE)

    elif line[:3] == 'dir':
        dir = line[4:]
        CWD[dir] = dict()

    else:
        fileReg = r"(?P<size>\d+) (?P<name>.+)"
        matched = re.match(fileReg, line)
        if bool(matched):
            file = matched.groupdict()
            CWD[file['name']] = int(file['size'])

def calc_dir_size(tree):
    dir_size = 0
    for node in tree:
        if type(node) == dict:
            dir_size += calc_dir_size(node)
        else:
            dir_size += node

    return dir_size

def pretty_tree(tree):
    import json
    return json.dumps(tree, indent=2)
    
def main():
    global DIR_SIZES
    with open(IN_PATH, 'r') as file:
        for line in file.readlines():
            parse_line(line.strip('\n'))

    DIR_SIZES = [calc_dir_size(get_by_path(FS, dir)) for dir in DIR_PATHS]

    print(pretty_tree(FS))

    puzzle1()
    puzzle2()

def puzzle1():

    max_size = 100000
    small_enough = [size for size in DIR_SIZES if size <= max_size]

    print("Puzzle 1:", sum(small_enough))

def puzzle2():
    total_size = 70000000
    req_size = 30000000
    used_size = calc_dir_size(FS)
    free = total_size - used_size
    to_free = req_size - free

    big_enough = [size for size in DIR_SIZES if size > to_free]
    print("Puzzle 2:", min(big_enough))


if __name__ == "__main__":
    main()
