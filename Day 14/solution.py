from collections import Counter

def part1():
    output = template
    for _ in range(10):
        output = perform_step(output)

    counter = Counter(output)
    return counter.most_common()[0][1] - counter.most_common()[-1][1]


def part2():
    pair_counts = Counter(list(get_char_pairs(template)))
    final_counts = Counter()

    for _ in range(40):
        new_pair_counts = Counter()
        for pair, counts in pair_counts.items():
            replacement = rules.get(pair)
            if rules.get(pair):
                new_pair_counts[f"{pair[0]}{replacement}"] += counts
                new_pair_counts[f"{replacement}{pair[1]}"] += counts
            else:
                new_pair_counts[pair] = counts
        pair_counts = new_pair_counts

    for pair, count in pair_counts.items():
        final_counts[pair[0]] += count
        final_counts[pair[1]] += count

    final_counts[template[-1]] += 1
    final_counts[template[0]] += 1
    return (final_counts.most_common()[0][1] // 2) - (final_counts.most_common()[-1][1] // 2)


def perform_step(input_string):
    new_string = input_string[0]
    for pair in get_char_pairs(input_string):
        if rules.get(pair):
            new_string += rules.get(pair) + pair[1]
    return new_string


def get_char_pairs(input_string):
    for x in range(len(input_string) - 1):
        yield input_string[x:x + 2]


if __name__ == '__main__':
    template = ""
    rules = {}

    for pos, line in enumerate(open('input.txt')):
        if line == '\n':
            continue
        if pos == 0:
            template = line.strip()
        else:
            key, value = line.strip().split(' -> ')
            rules[key] = value

    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
