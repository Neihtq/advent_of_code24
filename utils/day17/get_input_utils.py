from utils.input_path_utils import get_input_path


def get_input(test=False):
    input_path = get_input_path(17, test)
    with open(input_path) as file:
        lines = file.readlines()
        registers = {register : int(lines[i].strip().split(' ')[-1]) for i, register in enumerate([4, 5, 6])}
        program = [int(num) for num in lines[-1].strip().split(' ')[-1].split(',')]
        return registers, program
