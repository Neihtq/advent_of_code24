import time
import copy
from utils.time_utils import execute
from utils.day6.get_input_utils import get_input

OBSTACLE, EMPTY_FIELD, JUNCTION = '#', '.', '+'
OPPOSITE_ANGLE = {'-': '|', '|': '-'}


def get_starting_position(input_map):
    guard_directions = {
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1),
        'v': (1, 0)
    }
    for i in range(len(input_map)):
        for j in range(len(input_map[0])):
            guard = input_map[i][j]
            if guard in guard_directions: 
                return i, j, guard_directions[guard]


def turn_right(direction):
    if direction == (-1, 0):
        return 0, 1
    if direction == (0, 1):
        return 1, 0
    if direction == (1, 0):
        return 0, -1
    
    return -1, 0


def count_distinct_guard_positions(input_map):
    i, j, (i_dir, j_dir) = get_starting_position(input_map)
    visited_position = set()
    while (
        i >= 0 and i < len(input_map)
        and j >= 0 and j < len(input_map[0])
    ):
        visited_position.add((i, j))
        next_i, next_j = i + i_dir, j + j_dir
        if (
            next_i < 0 or next_i >= len(input_map)
            or next_j < 0 or next_j >= len(input_map[0])
        ):
            break

        front_field = input_map[next_i][next_j]
        if front_field is OBSTACLE:
            i_dir, j_dir = turn_right((i_dir, j_dir))

        i += i_dir
        j += j_dir

    return len(visited_position)



def is_loop(input_map, i, j, i_dir, j_dir):
    lines = set()
    prev_i, prev_j = i, j
    while (
        i >= 0 and i < len(input_map)
        and j >= 0 and j < len(input_map[0])
    ):
        next_i, next_j = i + i_dir, j + j_dir
        if (
            next_i < 0 or next_i >= len(input_map)
            or next_j < 0 or next_j >= len(input_map[0])
        ):
            break

        front_field = input_map[next_i][next_j]
        if front_field == OBSTACLE:
            line = (prev_i, prev_j, i, j)
            if line in lines:
                return True
            lines.add(line)
            i_dir, j_dir = turn_right((i_dir, j_dir))
            prev_i, prev_j = i, j
            continue

        i += i_dir
        j += j_dir

    return False


def count_obstructions(input_map):
    start_i, start_j, (start_i_dir, start_j_dir) = get_starting_position(input_map)
    i_dir, j_dir = start_i_dir, start_j_dir
    i, j = start_i, start_j
    
    obstruction = set()
    while (
        i >= 0 and i < len(input_map)
        and j >= 0 and j < len(input_map[0])
    ):
        next_i, next_j = i + i_dir, j + j_dir
        if (
            next_i < 0 or next_i >= len(input_map)
            or next_j < 0 or next_j >= len(input_map[0])
        ):
            break

        front_field = input_map[next_i][next_j]
        if front_field == OBSTACLE: 
            i_dir, j_dir = turn_right((i_dir, j_dir))
            continue
        if next_i != start_i or next_j != start_j:
            input_map[next_i][next_j] = OBSTACLE
            if is_loop(input_map, start_i, start_j, start_i_dir, start_j_dir):
                obstruction.add((next_i, next_j))
            input_map[next_i][next_j] = front_field

        i += i_dir
        j += j_dir

    print("Number of obstructions", len(obstruction))


def part1(input_map):
    num_distinct_positions = count_distinct_guard_positions(input_map)
    print("Number of distinct positions", num_distinct_positions)



def part2(input_map):
    count_obstructions(input_map)


def main():
    input_map = get_input()
    execute([part1, part2], input_map)


if __name__ == '__main__':
    main()