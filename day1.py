from collections import Counter
from utils.time_utils import execute
from utils.day1.get_input_utils import get_input


def part1(left_list, right_list):
    left_list.sort()
    right_list.sort()

    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])

    print("total distance", total_distance)


def part2(left_list, right_list):
    right_count = Counter(right_list)
    sim_score = 0
    for num in left_list:
        sim_score += num * right_count[num]

    print("similarity score", sim_score)

def main():
    left_list, right_list = get_input()
    execute([part1, part2], left_list, right_list)


if __name__ == '__main__':
    main()
