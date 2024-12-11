from collections import defaultdict, Counter
from utils.time_utils import execute
from utils.day11.get_input_utils import get_input


def blink(cache, stone_count):
    new_stones = []
    new_count = defaultdict(int)
    for stone, count in stone_count.items():
        if stone not in cache:
            if stone == '0':
                cache[stone] = ['1']
            elif len(stone) % 2 == 0:
                middle = len(stone) // 2
                left_stone = str(int(stone[:middle]))
                right_stone = str(int(stone[middle:]))
                cache[stone] = [left_stone, right_stone]
            else:
                cache[stone] = [str(int(stone) * 2024)]


        for new_stone in cache[stone]:
            new_count[new_stone] += count
            new_stones.append(new_stone)
    
    return new_count


def simulate_blinking(stones, num_blinks):
    cache = {}
    stone_count = Counter(stones)
    for _ in range(num_blinks):
        new_count = blink(cache, stone_count) 
        stone_count = new_count

    num_stones = sum(stone_count.values())
    print(f"Number of stones after {num_blinks} blinks", num_stones)


def part1(stones):
    simulate_blinking(stones, 25)


def part2(stones):
    simulate_blinking(stones, 75)


def main():
    stones = get_input()
    execute([part1], stones)
    execute([part1, part2], stones)


if __name__ == '__main__':
    main()