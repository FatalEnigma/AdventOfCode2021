from collections import deque
from math import prod


def part1():
    return sum(values[coords]+1 for coords in values.keys() if is_lower_than_neighbours(coords))


def is_lower_than_neighbours(coord_to_verify):
    return all(values[coord_to_check] > values[coord_to_verify] for coord_to_check in get_neighbours(coord_to_verify))


def get_neighbours(coord):
    x, y = coord
    return [coord for coord in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)] if values.get(coord) is not None]


def part2():
    low_points = [coords for coords in values.keys() if is_lower_than_neighbours(coords)]
    basin_sizes = []

    for point in low_points:
        visited = set()
        frontier = deque()
        frontier.append(point)
        visited.add(point)
        basin = [values[point]]

        while len(frontier):
            neighbours_for_point = get_neighbours(frontier.pop())
            for neighbour in neighbours_for_point:
                if neighbour not in visited:
                    visited.add(neighbour)
                    if values[neighbour] != 9:
                        frontier.append(neighbour)
                        basin.append(values[neighbour])
        basin_sizes.append(len(basin))
    return prod(sorted(basin_sizes)[-3:])


if __name__ == '__main__':
    values = {(x, y): int(height) for y, line in enumerate(open('input.txt')) for x, height in enumerate(line.strip())}
    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
