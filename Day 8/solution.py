def part1():
    return sum(1 for uniq_digits_list in values for digit in uniq_digits_list[1] if len(digit) in [2, 3, 4, 7])


def part2():
    return sum(decode_number(input_tuple) for input_tuple in values)


def decode_number(input_tuple):
    unique_codes, digits = input_tuple
    one = next(x for x in unique_codes if len(x) == 2)
    four = next(x for x in unique_codes if len(x) == 4)
    seven = next(x for x in unique_codes if len(x) == 3)
    eight = next(x for x in unique_codes if len(x) == 7)
    six = next(x for x in unique_codes if len(x) == 6 and not one.issubset(x))
    nine = next(x for x in unique_codes if len(x) == 6 and four.issubset(x))
    zero = next(x for x in unique_codes if len(x) == 6 and not six.issubset(x) and not nine.issubset(x))
    three = next(x for x in unique_codes if len(x) == 5 and seven.issubset(x))
    two = next(x for x in unique_codes if len(x) == 5 and len(four - x) == 2)
    five = next(x for x in unique_codes if len(x) == 5 and len(four - x) == 1 and not three.issubset(x))
    num_list = [zero, one, two, three, four, five, six, seven, eight, nine]
    decoded_num = ""
    for digit in digits:
        decoded_num += next(str(index) for index, num_set in enumerate(num_list) if num_set == digit)
    return int(decoded_num)


if __name__ == '__main__':
    values = tuple(tuple([[set(x) for x in line.strip().split(' | ')[0].split(' ')], [set(x) for x in line.strip().split(' | ')[1].split(' ')]]) for line in open("input.txt"))
    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
