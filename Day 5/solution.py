from collections import defaultdict


def part1():
    horiz_vert_lines = defaultdict(int)
    more_two_overlaps = 0
    for first, second in coord_gen():
        if is_horiz_or_vert(first, second):
            for point in get_coords_for_points(first, second):
                if horiz_vert_lines[point] == 1:
                    more_two_overlaps += 1
                horiz_vert_lines[point] += 1
    return more_two_overlaps


def part2():
    horiz_vert_lines = defaultdict(int)
    more_two_overlaps = 0
    for first, second in coord_gen():
        points = get_coords_for_points(first, second) if is_horiz_or_vert(first, second) else get_coords_for_points_diag(first, second)
        for point in points:
            if horiz_vert_lines[point] == 1:
                more_two_overlaps += 1
            horiz_vert_lines[point] += 1
    return more_two_overlaps


def coord_gen():
    for line in open("input.txt"):
        split_line = line.strip().split(" -> ")
        yield tuple(map(int, split_line[0].split(","))), tuple(map(int, split_line[1].split(",")))


def is_horiz_or_vert(coord_1, coord_2):
    return coord_1[0] == coord_2[0] or coord_1[1] == coord_2[1]


def get_coords_for_points(coord_1, coord_2):
    return [(x, y) for x in range(min(coord_1[0], coord_2[0]), max(coord_1[0], coord_2[0]) + 1) for y in range(min(coord_1[1], coord_2[1]), max(coord_1[1], coord_2[1]) + 1)]


def get_coords_for_points_diag(coord_1, coord_2):
    step_x = -1 if coord_1[0] > coord_2[0] else 1
    step_y = -1 if coord_1[1] > coord_2[1] else 1
    x_range = range(coord_1[0], coord_2[0] + step_x, step_x)
    y_range = range(coord_1[1], coord_2[1] + step_y, step_y)
    return [(x, y) for x, y in zip(x_range, y_range)]


if __name__ == '__main__':
    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
