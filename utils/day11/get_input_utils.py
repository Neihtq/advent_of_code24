from utils.input_path_utils import get_input_path


def get_input():
    input_path = get_input_path(11)
    with open(input_path) as file:
        return file.readline().strip().split(' ')
        