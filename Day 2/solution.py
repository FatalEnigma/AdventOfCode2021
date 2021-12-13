def part1():
    horiz = 0
    depth = 0
    for line in open("input.txt"):
        match line.strip().split():
            case "up", value:
                depth -= int(value)
            case "down", value:
                depth += int(value)
            case "forward", value:
                horiz += int(value)
    return horiz * depth


def part2():
    horiz = 0
    depth = 0
    aim = 0
    for line in open("input.txt"):
        match line.strip().split():
            case "up", value:
                aim -= int(value)
            case "down", value:
                aim += int(value)
            case "forward", value:
                horiz += int(value)
                depth += aim * int(value)
    return horiz * depth


if __name__ == '__main__':
    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
