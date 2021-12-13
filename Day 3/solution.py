def part1():
    counts = [0 for _ in range(len(values[0]))]
    for line in values:
        for pos, num in enumerate(line):
            counts[pos] += int(num)

    majority = len(values) / 2

    gam = "".join("1" if x > majority else "0" for x in counts)
    eps = "".join("1" if x == "0" else "0" for x in gam)
    return int(gam, 2) * int(eps, 2)


def part2():
    values_arr = [[int(num) for num in line] for line in values]
    oxy_gen = values_arr.copy()
    co2_scrub = values_arr.copy()

    for x in range(12):
        num_keep = 1 if sum(val[x] for val in oxy_gen) >= len(oxy_gen) / 2 else 0
        oxy_gen = [keep for keep in oxy_gen if keep[x] == num_keep]
        if len(oxy_gen) == 1:
            break

    for x in range(12):
        num_keep = 0 if sum(val[x] for val in co2_scrub) >= len(co2_scrub) / 2 else 1
        co2_scrub = [keep for keep in co2_scrub if keep[x] == num_keep]
        if len(co2_scrub) == 1:
            break

    return int("".join(str(x) for x in oxy_gen[0]), 2) * int("".join(str(x) for x in co2_scrub[0]), 2)


if __name__ == '__main__':
    values = [line.strip() for line in open("input.txt")]
    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
