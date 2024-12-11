from utils.input_path_utils import get_input_path


def get_input():
    input_path = get_input_path(1)
    with open(input_path) as file:
        lines = file.readlines()
        left_list, right_list = [], []
        for line in lines:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))

        return left_list, right_list
    