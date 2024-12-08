import os


def get_input_path(day: int):
    inputs_dir = "inputs"
    input_file_name = f"day{day}.txt"
    
    return os.path.join(inputs_dir, input_file_name)
