from utils.time_utils import execute
from utils.day2.get_input_utils import get_input


def are_safe(levels):
    is_inc = levels[0] < levels[1]
    prev = -1
    for level in levels:
        if prev == -1:
            prev = level
            continue
        if not is_safe(prev, level, is_inc):
            return False
       
        prev = level

    return True


def part1(levels):
    num_safe = 0
    for l in levels:
        if are_safe(l):
            num_safe += 1
    print("num safe", num_safe)


def is_safe(curr, succ, is_inc):
    diff = curr - succ
    
    if abs(diff) > 3 or (diff) == 0:
        return False
    if is_inc and diff > 0:
        return False
    if not is_inc and diff < 0:
        return False

    return True


def are_tolerable_safe(levels):
    unsafe_count = 0
    i = 1
    curr = levels[0]
    is_inc = levels[0] < levels[1]
    while i < len(levels):
        succ = levels[i]
        safe_pair = is_safe(curr, succ, is_inc)
        if safe_pair:
            curr = succ
        else:
            unsafe_count += 1

        if unsafe_count > 1:
            return False

        i += 1

    return True


def part2(levels):
    num_safe = 0
    for l in levels:
        if are_tolerable_safe(l):
            num_safe += 1
        elif are_tolerable_safe(list(reversed(l))):
            num_safe += 1
    
    print('num tolerable safe', num_safe)


def main():
    levels = get_input()
    execute([part1, part2], levels)


if __name__ == '__main__':
    main()
