from utils.input_path_utils import get_input_path


def get_input():
    input_path = get_input_path(14)
    robots = []
    with open(input_path) as file:
        for line in file.readlines():
            robot = {}
            segments = line.strip().split(' ')
            for i, segment in enumerate(segments):
                segment = segment.split('=')[-1].split(',')
                key_1, key_2 = 'x', 'y'
                if i == 1:
                    key_1, key_2 = 'x_dir', 'y_dir'
                robot[key_1] = int(segment[0])
                robot[key_2] = int(segment[1])

            robots.append(robot)

    return robots
