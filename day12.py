from collections import defaultdict
from utils.time_utils import execute
from utils.day12.get_input_utils import get_input

AREA = 0
PERIMETER = 1
VISITED = '#'

def create_dict():
    return [0, 0] 
    
    
def calc_price(plants):
    price = 0
    for area, perimeter in plants.values():
        price += area * perimeter

    return price


def get_perimeter(garden, trail, plants, current_plant, cluster_name):
    for (i, j) in trail:
        plants[cluster_name][AREA] += 1
        for i_dir, j_dir in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            adj_i, adj_j = i + i_dir, j + j_dir
            if is_out_ouf_bound(garden, adj_i, adj_j):
                plants[cluster_name][PERIMETER] += 1
                continue
            adj_field = garden[adj_i][adj_j]
            if adj_field != current_plant:
                plants[cluster_name][PERIMETER] += 1
    mark_fields(garden, trail)


def mark_fields(garden, trail):
    for (i, j) in trail:
        garden[i][j] = VISITED


def part1(garden):
    plants = defaultdict(create_dict)
    def get_cluster(i, j, current_plant, trail):
        if is_out_ouf_bound(garden, i, j):
            return
        if garden[i][j] != current_plant or (i, j) in trail:
            return
        
        trail.add((i, j))
        for i_dir, j_dir in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            adj_i, adj_j = i + i_dir, j + j_dir
            get_cluster(adj_i, adj_j, current_plant, trail)

    for i in range(len(garden)):
        for j in range(len(garden[i])):
            current_plant = garden[i][j]
            if garden[i][j] != VISITED:
                trail = set()
                get_cluster(i, j, current_plant, trail)
                cluster_name = f'{current_plant}{i}{j}'
                get_perimeter(garden, trail, plants, current_plant, cluster_name)
    
    price = calc_price(plants)
    print("Price", price)


def get_num_corners(garden, i, j):
    directions = {
        'down': (1,0),
        'up': (-1,0),
        'right': (0,1),
        'left': (0,-1),
        'downright': (1,1),
        'upright': (-1, 1),
        'downleft': (1,-1),
        'upleft': (-1, -1)
    }
    adj_points = {}
    for direction, (i_dir, j_dir) in directions.items():
        adj_i, adj_j = i + i_dir, j + j_dir
        if is_out_ouf_bound(garden, adj_i, adj_j):
            adj_points[direction] = '#'
        else:
            adj_point = garden[adj_i][adj_j]
            adj_points[direction] = adj_point

    corner_directions = [
        ('left', 'up', 'upleft'),
        ('up', 'right', 'upright'),
        ('down', 'right', 'downright'),
        ('down', 'left', 'downleft'),
    ]

    bool_mat = []
    for shape in corner_directions:
        neighbours = [adj_points[direction] for direction in shape[:-1]]
        is_corner = True
        for point in neighbours:
            is_corner = point != garden[i][j] and is_corner
        
        bool_mat.append(is_corner)
    num_outside_corners = sum(bool_mat)

    bool_mat = []
    for shape in corner_directions:
        neighbours = [adj_points[direction] for direction in shape[:-1]]
        is_corner = True
        for point in neighbours:
            is_corner = point == garden[i][j] and is_corner

        diag_neighbour = adj_points[shape[-1]]
        is_corner = diag_neighbour != garden[i][j] and is_corner

        bool_mat.append(is_corner)
    num_inside_corners = sum(bool_mat)

    return num_outside_corners + num_inside_corners
    

def is_out_ouf_bound(garden, i, j):
    return i >= len(garden) or i < 0 or j >= len(garden[0]) or j < 0


def create_type_map():
    return {
        'type1': [],
        'type2': []
    }

def part2(garden):
    visited_matrix = [ ['. ' for _ in row] for row in garden]
    def get_cluster(i, j, current_plant, trail):
        if is_out_ouf_bound(garden, i, j):
            return
        if garden[i][j] != current_plant or (i, j) in trail:
            return
        
        trail.add((i, j))
        for i_dir, j_dir in [(1,0), (-1, 0), (0, 1), (0, -1)]:
            adj_i, adj_j = i + i_dir, j + j_dir
            get_cluster(adj_i, adj_j, current_plant, trail)


    clusters = {}
    for i in range(len(garden)):
        for j in range(len(garden[i])):
            current_plant = garden[i][j]
            if visited_matrix[i][j] != VISITED:
                trail = set()
                get_cluster(i, j, current_plant, trail)
                cluster_name = f'{current_plant}{i}{j}'
                clusters[cluster_name] = trail
                mark_fields(visited_matrix, trail)

    anker_points = defaultdict(int)
    for k in clusters:
        points = clusters[k]
        for i, j in points:
            anker_points[k] += get_num_corners(garden, i, j)

    price = 0
    for k in clusters:
        area = len(clusters[k])
        num_sides = anker_points[k]
        price += area * num_sides

    print("discounted price", price)


def main():
    garden = get_input()
    execute([part1], garden)
    garden = get_input()
    execute([part2], garden)


if __name__ == '__main__':
    main()
