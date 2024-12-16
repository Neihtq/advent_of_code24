from utils.input_path_utils import get_input_path
from utils.input_grid_utils import get_grid


def get_input(test=False):
    input_path = get_input_path(16, test=test)
    return get_grid(input_path)
