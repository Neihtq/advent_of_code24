from collections import defaultdict
from utils.time_utils import execute
from utils.day8.get_input_utils import get_input

EMPTY_FIELD = '.'


def get_sample_input():
    sample = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    return [list(line.strip()) for line in sample.split('\n')]


def part1(grid):
    unique_positions = set()
    tower_positions = get_tower_positions(grid) 

    for frequency in tower_positions:
        points = tower_positions[frequency]
        for i in range(len(points)):
            pt1 = points[i]
            for j in range(i+1, len(points)):
                pt2 = points[j]
                antinode_1 = get_antinode_position(pt1, pt2)
                sack(grid, antinode_1, unique_positions)
                antinode_2 = get_antinode_position(pt2, pt1)
                sack(grid, antinode_2, unique_positions)

    print("Number unique anti node positions", len(unique_positions))


def get_directions(pt1, pt2):
    i_dir = pt1[0] - pt2[0]
    j_dir = pt1[1] - pt2[1]

    return (i_dir, j_dir)


def get_antinode(pt, i_dir, j_dir):
    return (pt[0] + i_dir, pt[1] + j_dir)


def get_antinode_position(pt1, pt2):
    i_dir, j_dir = get_directions(pt1, pt2)
    return get_antinode(pt1, i_dir, j_dir)


def sack(grid, antinode, unique_positions):
    i, j = antinode[0], antinode[1]
    i_out_ouf_bound = i >= len(grid) or i < 0
    j_out_ouf_bound = j >= len(grid[0]) or j < 0
    if not i_out_ouf_bound and not j_out_ouf_bound:
        unique_positions.add(antinode)


def get_tower_positions(grid):
    tower_positions = defaultdict(list)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            field = grid[i][j]
            if field != EMPTY_FIELD:
                tower_positions[field].append((i, j))

    return tower_positions



def get_antinodes(grid, pt1, pt2, unique_positions):
    i, j = pt1[0], pt1[1]
    i_dir, j_dir = get_directions(pt1, pt2)

    while i < len(grid) and i >= 0 and j < len(grid[0]) and j >= 0:
        antinode = get_antinode((i, j), i_dir, j_dir)
        i, j = antinode
        sack(grid, antinode, unique_positions)


def part2(grid):
    unique_positions = set()
    tower_positions = get_tower_positions(grid) 
    for frequency in tower_positions:
        points = tower_positions[frequency]
        for i in range(len(points)):
            pt1 = points[i]
            unique_positions.add(pt1)
            for j in range(i+1, len(points)):
                get_antinodes(grid, pt1, points[j], unique_positions)
                get_antinodes(grid, points[j], pt1, unique_positions)

    print("Updated number unique anti node positions", len(unique_positions))


def main():
    grid = get_input()
    execute([part1, part2], grid)


if __name__ == '__main__':
    main()
