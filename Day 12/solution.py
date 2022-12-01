from collections import deque
from collections import defaultdict


def part1():
    state = deque([('start', {'start'}, ['start'])])

    num_paths = 0

    while state:
        next_cave, visited_small, path = state.popleft()

        if next_cave == 'end':
            num_paths += 1
            continue

        for neighbour in values[next_cave]:
            if neighbour not in visited_small:
                new_small_set = set(visited_small)
                if neighbour.lower() == neighbour:
                    new_small_set.add(neighbour)
                new_path = [*path, neighbour]
                state.append((neighbour, new_small_set, new_path))
    return num_paths


def part2():
    state = deque([('start', ['start'], ['start'])])

    num_paths = 0

    while state:
        next_cave, visited_small, path = state.popleft()

        if next_cave == 'end':
            num_paths += 1
            continue

        for neighbour in values[next_cave]:
            if len(set(visited_small)) in [len(visited_small), len(visited_small) - 1] and neighbour != 'start':
                new_small_list = [*visited_small]
                if neighbour.lower() == neighbour:
                    new_small_list.append(neighbour)
                new_path = [*path, neighbour]
                state.append((neighbour, new_small_list, new_path))
    return num_paths


if __name__ == '__main__':
    values = defaultdict(set)
    for line in open('input.txt'):
        if line == '\n':
            continue
        src, dest = line.strip().split('-')
        values[src].add(dest)
        values[dest].add(src)

    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
