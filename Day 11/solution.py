from itertools import count
from copy import deepcopy


def part1():
    values = deepcopy(master_values)
    return sum(perform_step(values) for _ in range(100))


def part2():
    values = deepcopy(master_values)
    return next(x for x in count(1) if perform_step(values) == 100)


def perform_step(values):
    to_flash = set()
    for y in range(10):
        for x in range(10):
            values[x, y] += 1
            if values[x, y] > 9:
                to_flash.add((x, y))

    return sum(flash(coords, values) for coords in to_flash)


def get_non_flashed_neighbours(coords, values):
    x, y = coords
    return [coords for coords in [(x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1), (x, y-1), (x+1, y-1)] if values.get(coords) is not None
            and values.get(coords) != 0]


def flash(coords, values):
    total_flashes = 0
    x, y = coords
    if values[x, y] == 0:
        return 0
    total_flashes += 1
    values[x, y] = 0
    for neighbour in get_non_flashed_neighbours(coords, values):
        if values[neighbour] == 0:
            continue
        values[neighbour] += 1
        if values[neighbour] > 9:
            total_flashes += flash(neighbour, values)
    return total_flashes


if __name__ == '__main__':
    master_values = {(x, y): int(height) for y, line in enumerate(open('input.txt')) for x, height in enumerate(line.strip())}
    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
