import heapq
from collections import defaultdict
from utils.time_utils import execute
from utils.day9.get_input_utils import get_input

EMPTY_FIELD = '.'


def get_file_system(disk_map: str):
    file_system = []
    file_id = 0
    for i in range(len(disk_map)):
        num = int(disk_map[i])
        if i % 2 == 0:
            file_system.extend(num * [file_id])
            file_id += 1
        else:
            file_system.extend(num * [EMPTY_FIELD])

    return file_system


def compact_file_system(file_system):
    left, right = 0, len(file_system) - 1
    while left != right:
        if file_system[left] == EMPTY_FIELD:
            file_system[left], file_system[right] = file_system[right], file_system[left]
            while file_system[right] == EMPTY_FIELD:
                right -= 1
        left += 1 


def get_checksum(file_system):
    checksum = 0
    string = ""
    for i, x in enumerate(file_system):
        if x != EMPTY_FIELD:
            checksum += (i * x)
            string += f' + {i} * {x}'

    return checksum


def part1(disk_map):
    file_system = get_file_system(disk_map)
    compact_file_system(file_system)
    checksum = get_checksum(file_system)
    print("checksum", checksum)


def part2(disk_map):
    spaces, files = [], []
    for i in range(len(disk_map)):
        if i % 2 == 0:
            # (index, value, should_ignore)
            files.append([i, int(disk_map[i]), False])
        else:
            spaces.append([i, int(disk_map[i])])
    
    mapping = defaultdict(list)
    for i in range(len(files) - 1, -1, -1):
        file_id_doubled, num_files, _ = files[i]
        for j in range(i):
            index, num_spaces = spaces[j]
            if num_files <= num_spaces and file_id_doubled > index:
                mapping[index].append((file_id_doubled, num_files))
                spaces[j][1] -= num_files
                files[i][2] = True
                break

    file_system = []
    space_ptr, file_ptr = 0, 0
    for i in range(len(disk_map)):
        if i % 2 == 0:
            file_id_doubled, num_files, should_ignore = files[file_ptr]
            if not should_ignore:
                file_system.extend(num_files * [file_id_doubled // 2])
            else:
                file_system.extend(num_files * [EMPTY_FIELD])
            file_ptr += 1
        else:
            index, num_spaces = spaces[space_ptr]
            if index in mapping:
                for file_id_doubled, num_files in mapping[index]:
                    file_system.extend(num_files * [file_id_doubled // 2])
            file_system.extend(num_spaces * [EMPTY_FIELD])
            space_ptr += 1

    checksum = get_checksum(file_system) 
    print("Checksum unfragmented", checksum)


def get_heaps(file_system):
    min_heaps = defaultdict(list)
    left, right = 0, 0
    left = 0
    while left < len(file_system):
        if file_system[left] == EMPTY_FIELD:
            right = left + 1
            while right < len(file_system) and file_system[right] == EMPTY_FIELD:
                right += 1
            length = right - left
            min_heaps[length].append((left, right))
            left = right
        else:
            left += 1
    
    return min_heaps


def optimized_p2(disk_map):
    file_system = get_file_system(disk_map)
    min_heaps = get_heaps(file_system)


def main():
    # disk_map = get_input()
    disk_map = "2333133121414131402"
    optimized_p2(disk_map)
    # execute([part1, part2], disk_map)


if __name__ == '__main__':
    main()
