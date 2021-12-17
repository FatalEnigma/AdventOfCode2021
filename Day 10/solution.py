from collections import deque


def part1():
    scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return sum(scoring[get_first_corrupt_char(entry)] for entry in values if get_first_corrupt_char(entry) is not None)


def part2():
    scores = sorted([get_score_for_chars(get_closing_chars(entry)) for pos, entry in enumerate(values) if pos not in corrupted_line_index])
    return scores[len(scores) // 2]


def get_score_for_chars(chars):
    scoring = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0

    for char in chars:
        score = (score * 5) + scoring[char]
    return score


def get_closing_chars(entry):
    stack = deque()
    valid_open = ['(', '[', '{', '<']
    valid_close = [')', ']', '}', '>']

    for char in entry:
        if char in valid_open:
            stack.append(char)
        elif char in valid_close:
            stack.pop()

    closing_chars = ""
    for _ in range(len(stack)):
        closing_chars += valid_close[valid_open.index(stack.pop())]
    return closing_chars


def get_first_corrupt_char(entry):
    stack = deque()
    valid_open = ['(', '[', '{', '<']
    valid_close = [')', ']', '}', '>']

    for char in entry:
        if char in valid_open:
            stack.append(char)
        elif char in valid_close:
            last_open = stack.pop()
            if valid_close.index(char) != valid_open.index(last_open):
                corrupted_line_index.add(values.index(entry))
                return char
    return None


if __name__ == '__main__':
    values = [line.strip() for line in open('input.txt')]
    corrupted_line_index = set()
    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
