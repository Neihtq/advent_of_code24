from utils.input_path_utils import get_input_path


def get_input():
    input_path = get_input_path(18)
    with open(input_path) as file:
        lines = file.readlines()
        output = []
        for line in lines:
            x, y = line.strip().split(',')
            output.append((int(y), int(x)))
        
        return output
