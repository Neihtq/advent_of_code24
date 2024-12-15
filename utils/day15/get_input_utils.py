from utils.input_path_utils import get_input_path


def get_input(test=False):
    input_path = get_input_path(15, test)
    warehouse_map = []
    robot_moves = []
    with open(input_path) as file:
        lines = file.readlines()
        target_list = warehouse_map
        for line in lines:
            if line == '\n':
                target_list = robot_moves
            else:
                target_list.append(line.strip())

    warehouse_map = [[field for field in row] for row in warehouse_map] 
    robot_moves = ''.join(robot_moves) 
    
    return warehouse_map, robot_moves
    