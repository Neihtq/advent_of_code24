from utils.input_path_utils import get_input_path


def get_input():
    input_path = get_input_path(7)
    with open(input_path) as file:
        lines = file.readlines()
        out = []
        for line in lines:
            equation_str = line.strip().split(' ')
            result = int(equation_str[0][:-1])
            nums = [int(num) for num in equation_str[1:]]
            out.append((result, nums))

        return out
