from utils.input_path_utils import get_input_path


def get_input():
    input_path = get_input_path(13)
    with open(input_path) as file:
        lines = file.readlines()
        return lines
