from collections import Counter


def part1():
    fish_list = [initial_counts[str(x)] if initial_counts.get(str(x)) else 0 for x in range(9)]
    return simulate_days(80, fish_list)


def part2():
    fish_list = [initial_counts[str(x)] if initial_counts.get(str(x)) else 0 for x in range(9)]
    return simulate_days(256, fish_list)


def simulate_days(days, fish_list):
    for _ in range(days):
        num_zero = fish_list.pop(0)
        fish_list[6] += num_zero
        fish_list.append(num_zero)
    return sum(fish_list)


if __name__ == '__main__':
    initial_counts = {}
    for line in open("input.txt"):
        initial_counts = Counter(line.strip().split(","))

    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
