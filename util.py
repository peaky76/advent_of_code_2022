from collections import defaultdict
from itertools import chain

def draw(coord_lists, symbols, bottom_bound_symbol = None):
    all_coords = list(chain(*coord_lists))
    min_x = min([coord[0] for coord in all_coords]) - 1
    max_x = max([coord[0] for coord in all_coords]) + 2
    min_y = min([coord[1] for coord in all_coords]) - 1
    max_y = max([coord[1] for coord in all_coords]) + 2

    output_dict = defaultdict(lambda: '.')
    for i, coord_list in enumerate(coord_lists):
        output_dict.update({(x, y): symbols[i] for (x, y) in coord_list})
    
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            if bottom_bound_symbol and y == max_y - 1:
                print(bottom_bound_symbol, end='')
            else:
                print(output_dict[(x, y)], end='')
        
        print('\n')