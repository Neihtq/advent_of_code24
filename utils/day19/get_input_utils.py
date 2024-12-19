from utils.input_path_utils import get_input_path


def get_input(test=False):
    input_path = get_input_path(19, test=test)
    
    with open(input_path) as file:
        lines = file.readlines()

        available = set([stripes.strip() for stripes in lines[0].strip().split(',')])
        designs = [line.strip() for line in lines[2:]]

        return available, designs
