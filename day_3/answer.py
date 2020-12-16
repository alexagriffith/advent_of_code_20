def read_input():
    map = []
    f = open("input.txt", "r")
    for line in f:
        map.append(list(line.strip()))
    f.close()
    return map


def find_coords(end_x, end_y, slope_x, slope_y):
    coords = [(0, 0)]
    coord_x, coord_y = next_coord(0, 0, slope_x, slope_y)
    while coord_y < end_y:
        coords.append((coord_x, coord_y))
        coord_x, coord_y = next_coord(coord_x, coord_y, slope_x, slope_y)
        if coord_x > end_x:
            coord_x = coord_x - end_x - 1  # we start at 0
    return coords


def next_coord(x1, y1, slope_x, slope_y):
    return x1 + slope_x, y1 + slope_y


def count_trees(map, coords):
    num_trees = 0
    num_empty = 0
    for coord in coords:
        x = coord[0]
        y = coord[1]
        if map[y][x] == '#':
            num_trees += 1
        elif map[y][x] == '.':
            num_empty += 1
    return num_trees, num_empty, num_empty + num_trees


if __name__ == '__main__':
    # this problem would be much better if I made it a class.
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    map = read_input()
    result = 1
    for slope in slopes:
        coords = find_coords(len(map[0]) - 1, len(map), slope[0], slope[1])
        num_trees, num_empty, total = count_trees(map, coords)
        print(f" slope ({slope[0]}, {slope[1]})trees: {num_trees}, empty {num_empty}, total {total}")
        result *= num_trees
    print(result)

