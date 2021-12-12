def get_value_pairs(input_values, window_size):
    for x in range(len(input_values) - window_size):
        yield sum(input_values[x:x+window_size]), sum(input_values[x+1:x+1+window_size])


def part1():
    return sum(1 for entry in get_value_pairs(values, 1) if entry[1] > entry[0])


def part2():
    return sum(1 for entry in get_value_pairs(values, 3) if entry[1] > entry[0])


if __name__ == '__main__':
    values = [int(line.strip()) for line in open("input.txt")]
    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
