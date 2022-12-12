import os
import numpy as np

INPUT = "input"
# INPUT = "test"
IN_PATH = os.path.join(os.path.dirname(__file__), INPUT)


def parse_grid(lines):
    grid = [list(map(int, list(line))) for line in lines]
    return np.array(grid)

def get_top(i,j,grid):
    return np.flip(grid[:i, j])

def get_bot(i,j,grid):
    return grid[i+1:,j]

def get_left(i,j,grid):
    return np.flip(grid[i,:j])

def get_right(i,j,grid):
    return grid[i,j+1:]

def dist_to_nearest(tree, row):
    if len(row) == 0:
        return 0
    row_as_high = list(np.where(row >= tree))
    if len(row_as_high[0]) == 0:
        return len(row)
    return row_as_high[0][0] + 1

def is_tallest(i,j, grid):
    if i == 0 or i == grid.shape[0]-1 or j == 0 or j == grid.shape[1]-1:
        return True

    tree = grid[i, j]
    checkLeft = max(get_left(i,j,grid)) < tree
    checkRight = max(get_right(i,j,grid)) < tree
    checkTop = max(get_top(i,j,grid)) < tree
    checkTopBottom = max(get_bot(i,j,grid)) < tree
    
    isVisible = any([checkRight, checkLeft, checkTop, checkTopBottom])

    return isVisible

def calc_scenic_score(i,j, grid):
    
    tree = grid[i,j]
    score_left = dist_to_nearest(tree, get_left(i,j,grid))
    score_right = dist_to_nearest(tree, get_right(i,j,grid))
    score_top = dist_to_nearest(tree, get_top(i,j,grid))
    score_bot = dist_to_nearest(tree, get_bot(i,j,grid))

    return score_left * score_right * score_top * score_bot

def main():
    global DIR_SIZES
    with open(IN_PATH, 'r') as file:
        grid = parse_grid([line.strip('\n') for line in file.readlines()])
    
    nVisible = 0
    top_scene_score = 0
    for (i,j), tree in np.ndenumerate(grid):
        nVisible += is_tallest(i,j,grid)
        score = calc_scenic_score(i,j,grid)
        if score > top_scene_score:
            top_scene_score = score

    print("puzzle 1:", nVisible)
    print("puzzle 2:", top_scene_score)
    

if __name__ == "__main__":
    main()
