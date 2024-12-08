from utils.input_path_utils import get_input_path


def get_input():
    input_path = get_input_path(2)

    with open(input_path) as file:
        levels = [
            list(map(int, line.split()))
            for line in file.readlines()
        ]
        return levels 
