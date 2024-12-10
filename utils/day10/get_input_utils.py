from utils.input_path_utils import get_input_path
from utils.input_grid_utils import get_grid


def get_input():
    input_path = get_input_path(10)
    grid = get_grid(input_path)
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = int(grid[i][j]) 

    return grid


def get_sample():
    sample_str = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
    grid = [list(line.strip()) for line in sample_str.split('\n')]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = int(grid[i][j]) 

    return grid


def get_small_sample():
    sample_str = """0123
1234
8765
9876"""
    grid = [list(line.strip()) for line in sample_str.split('\n')]
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = int(grid[i][j]) 

    return grid
