def part1():
    return min(sum(abs(crab-x) for crab in crabs) for x in range(min(crabs), max(crabs)+1))


def part2():
    return min(sum((abs(crab-x) * (abs(crab-x) + 1)) // 2 for crab in crabs) for x in range(min(crabs), max(crabs)+1))


if __name__ == '__main__':
    for line in open('input.txt'):
        crabs = list(map(int, line.strip().split(',')))

    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
