import os


def get_input_path(day: int, test=False):
    inputs_dir = "inputs"
    input_file_name = f"day{day}.txt"
    if test:
        input_file_name = f"test_{input_file_name}"
    
    return os.path.join(inputs_dir, input_file_name)
