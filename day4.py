from utils.time_utils import execute
from utils.day4.get_input_utils import get_input


def part1(puzzle):
    ref_word = 'XMAS'
    ref_ptr = 0
    total_count = 0

    def dfs_traverse(row, col, row_dir, col_dir):
        nonlocal total_count
        nonlocal ref_ptr
        ref_ptr += 1
        if ref_ptr == len(ref_word):
            total_count += 1
            ref_ptr = 0
            return

        if col < 0 or row < 0 or row >= len(puzzle) or col >= len(puzzle[0]) :
            ref_ptr = 0
            return

        if puzzle[row][col] == ref_word[ref_ptr]:
            dfs_traverse(row + row_dir, col + col_dir, row_dir, col_dir)

        ref_ptr = 0

    row = 0
    while row < len(puzzle):
        col = 0
        while col < len(puzzle[row]):
            if puzzle[row][col] == ref_word[ref_ptr]:
                dfs_traverse(row, col + 1, 0, 1)
                dfs_traverse(row, col - 1, 0, -1)
                dfs_traverse(row + 1, col, 1, 0)
                dfs_traverse(row + 1, col + 1, 1, 1)
                dfs_traverse(row - 1, col + 1, -1, 1)
                dfs_traverse(row - 1, col - 1, -1, -1)
                dfs_traverse(row + 1, col - 1, 1, -1)
                
            col += 1
        row += 1
    
    print("num of XMAS", total_count)


def check_diagonal(puzzle, row, col, row_dir, col_dir, refs):
    if not refs:
        return True
    
    if puzzle[row+row_dir][col+col_dir] in refs:
        refs.remove(puzzle[row+row_dir][col+col_dir])
        return check_diagonal(puzzle, row, col, -1 * row_dir, -1 * col_dir, refs)
    
    return False


def check_cross(puzzle, row, col):
    left_valid = check_diagonal(puzzle, row, col, -1, -1, {'M', 'S'})
    right_valid = check_diagonal(puzzle, row, col, -1, 1, {'M', 'S'})
    if left_valid and right_valid:
        return 1 
    
    return 0


def part2(puzzle):
    total_count = 0
    for row in range(1, len(puzzle) - 1):
        for col in range(1, len(puzzle[0]) - 1):
            if puzzle[row][col] == 'A':
                total_count += check_cross(puzzle, row, col)

    print("number X-MAS", total_count)


def main():
    puzzle = get_input()
    execute([part1, part2], puzzle)


if __name__ == '__main__':
    main()
