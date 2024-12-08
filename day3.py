from utils.time_utils import execute
from utils.day3.get_input_utils import get_input


def scan_uncorrupted(instruction):
    nums = set([ str(i) for i in range(10)])
    run_sum = 0

    def is_valid_digit(s, i, ref, factor):
        nonlocal run_sum
        digits_limit = 3
        number = ''
        while len(number) <= digits_limit:
            if s[i] == ref and len(number) == 0:
                return i
            if s[i] == ref and ref == ',':
                return is_valid_digit(s, i+1, ')', int(number))
            if s[i] == ref and ref == ')':
                run_sum += int(number) * factor
                return i
            if s[i] not in nums:
                return i

            number += s[i]
            i += 1

        return i

    def is_mul(s, i):
        ref = 'mul('
        j = 0
        while i < len(s):
            if j == len(ref):
                i = is_valid_digit(s, i, ',', 1)
                j = 0
            if s[i] == ref[j]:
                j += 1
            else:
                j = 0

            i += 1

    is_mul(instruction, 0)
    return run_sum


def part1(memory):
    result = 0
    for s in memory:
        result += scan_uncorrupted(s)
    
    print("uncorrupted multiplication result", result)


def part2(memory):
    should_do = True
    nums = set([ str(i) for i in range(10)])
    run_sum = 0

    def is_valid_digit(s, i, ref, factor):
        nonlocal run_sum
        digits_limit = 3
        number = ''
        while len(number) <= digits_limit:
            if s[i] == ref and len(number) == 0:
                return i
            if s[i] == ref and ref == ',':
                return is_valid_digit(s, i+1, ')', int(number))
            if s[i] == ref and ref == ')':
                run_sum += int(number) * factor
                return i
            if s[i] not in nums:
                return i

            number += s[i]
            i += 1

        return i

    def parse_mul(s, i):
        ref = 'mul('
        j = 0
        while i < len(s):
            if j == len(ref):
                return is_valid_digit(s, i, ',', 1)
            if s[i] == ref[j]:
                j += 1
            else:
                return i

            i += 1

        return i

    def parse_do(s, i):
        nonlocal should_do
        ref = "do()"
        j = 0
        while i < len(s):
            if s[i] == ref[j]:
                j += 1
            elif s[i] == 'n' and j == 2:
                return parse_dont(s, i)
            else:
                return i
            
            if j == len(ref):
                should_do = True
                return i

            i += 1

        return i

    def parse_dont(s, i):
        nonlocal should_do
        ref = "n't()"
        j = 0
        while i < len(s):
            if s[i] == ref[j]:
                j += 1
            else:
                return i
            
            if j == len(ref):
                should_do = False
                return i

            i += 1
        
        return i

    def parse_instruction(s):
        i = 0
        while i < len(s):
            if should_do:
                if s[i] == 'd':
                    i = parse_do(s, i)
                if s[i] == 'm':
                    i = parse_mul(s, i)
            else:
                if s[i] == 'd':
                    i = parse_do(s,i)
            
            i += 1
    
    for instruction in memory:
        parse_instruction(instruction)
    
    print("enabled multiplication resul", run_sum)


def main():
    memory = get_input() 
    execute([part1, part2], memory)


if __name__ == '__main__':
    main()
