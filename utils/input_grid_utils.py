def get_grid(input_path):
    with open(input_path) as file:
        lines = file.readlines()
        
        return [list(line.strip()) for line in lines]
