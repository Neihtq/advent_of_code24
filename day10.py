from utils.time_utils import execute
from utils.day10.get_input_utils import get_input


def is_out_of_bound(topo_map, i, j):
    if i >= len(topo_map) or i < 0 or j >= len(topo_map[0]) or j < 0:
        return True

    return False


def traverse_trail(topo_map, i, j, trail_ends):
    field = topo_map[i][j]
    if field == 9:
        trail_ends.add((i, j))
        return 1

    total_sum = 0
    for i_dir, j_dir in [(0,1), (0, -1), (1, 0), (-1, 0)]:
        new_i, new_j = i + i_dir, j + j_dir
        if not is_out_of_bound(topo_map, new_i, new_j):
            if topo_map[new_i][new_j] == (field + 1):
                total_sum += traverse_trail(topo_map, new_i, new_j, trail_ends)

    return total_sum


def part1(topo_map):
    sum_score = 0
    for i in range(len(topo_map)):
        for j in range(len(topo_map[i])):
            if topo_map[i][j] == 0:
                trail_ends = set()
                traverse_trail(topo_map, i, j, trail_ends)
                sum_score += len(trail_ends)


    print("Sum of scores of all trailheads", sum_score)


def part2(topo_map):
    sum_rating = 0
    for i in range(len(topo_map)):
        for j in range(len(topo_map[i])):
            if topo_map[i][j] == 0:
                trail_ends = set()
                sum_rating += traverse_trail(topo_map, i, j, trail_ends)

    print("Sum of scores of all trailheads", sum_rating)


def main():
    topo_map = get_input()
    execute([part1, part2], topo_map)



if __name__ == '__main__':
    main()
