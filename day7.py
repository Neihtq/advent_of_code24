import itertools
from utils.day7.get_input_utils import get_input
from utils.time_utils import execute


def concatenate(left, right):
    length = 0 
    while left > 0:
        left = left // 10
        length += 1

    factor = 10 ** length
    result = left * factor + right
    
    return result


def simulate(nums, ops):
    result = nums[0]
    pairs = zip(nums[1:], ops)

    for num, op in pairs:
        if op == '+':
            result += num
        if op == '*':
            result *= num
        if op == '||':
            result = int(str(result) + str(num))
    
    return result


def can_be_true(result, nums, operations):
    combinations = itertools.product(operations, repeat=len(nums)-1)

    for combo in combinations:
        if result == simulate(nums, combo):
            return True

    return False


def calibrate(operations, puzzle):
    calibration_result = 0
    for equation in puzzle:
        if can_be_true(equation[0], equation[1], operations):
            calibration_result += equation[0]

    return calibration_result


def part1(puzzle):
    operations = ['+', '*']
    calibration_result = calibrate(operations, puzzle)
    print("Calibration Result", calibration_result)


def part2(puzzle):
    operations = ['+', '*', '||']
    calibration_result = calibrate(operations, puzzle)
    print("Calibration Result", calibration_result)


def main():
    puzzle = get_input()
    execute([part1, part2], puzzle)

if __name__ == '__main__':
    main()
