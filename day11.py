from utils.time_utils import execute
from utils.day11.get_input_utils import get_input


def blink(stones, cache):
    new_stones = []
    for stone in stones:
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

        new_stones.extend(cache[stone]) 
        
    
    return new_stones


def part1(stones):
    num_blinks = 10
    new_stones = stones
    cache = {}
    for _ in range(num_blinks):
        new_stones = blink(new_stones, cache) 

    print(f"Number of stones after {num_blinks} blinks", len(new_stones))


def part2(stones):
    num_blinks = 75
    new_stones = stones
    cache = {}
    for i in range(num_blinks):
        print('blink', i)
        new_stones = blink(new_stones, cache) 

    print(f"Number of stones after {num_blinks} blinks", len(new_stones))


def main():
    stones = get_input()
    # stones = ['125', '17']
    execute([part1, part2], stones)


if __name__ == '__main__':
    main()