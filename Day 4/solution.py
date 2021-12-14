import copy


def part1():
    board_list_copy = copy.deepcopy(board_list)
    for num in nums:
        for board in board_list_copy:
            coord = check_board(board, num)
            if coord and has_won(board, (coord[0], coord[1])):
                return sum(int(board[x][y][0]) for y in range(5) for x in range(5) if board[x][y][1] == 'unchecked') * int(num)


def part2():
    board_list_copy = [[board, False] for board in copy.deepcopy(board_list)]
    num_won = 0

    for num in nums:
        for pos, (board, won) in enumerate(board_list_copy):
            if won:
                continue
            coord = check_board(board, num)
            if coord and has_won(board, (coord[0], coord[1])):
                num_won += 1
                board_list_copy[pos][1] = True

                if num_won == len(board_list_copy):
                    return sum(int(board[x][y][0]) for y in range(5) for x in range(5) if board[x][y][1] == 'unchecked') * int(num)


def print_board(board):
    for y in range(5):
        print()
        for x in range(5):
            print(board[x][y], end=" ")
    print()
    print()


def process_input():
    numbers = values[0].split(",")
    boards = []

    for x in range(2, len(values) - 4, 6):
        board = [[], [], [], [], []]
        for row in values[x: x+5]:
            for pos, row_num in enumerate(row.split()):
                board[pos].append([row_num, "unchecked"])
        boards.append(board)
    return numbers, boards


def has_won(board_to_check, checked_coord):
    x_checked, y_checked = checked_coord
    return all(board_to_check[x][y_checked][1] == 'checked' for x in range(5)) or all(board_to_check[x_checked][y][1] == 'checked' for y in range(5))


def check_board(board, num):
    for x in range(5):
        for y in range(5):
            if board[x][y][0] == num:
                board[x][y][1] = 'checked'
                return x, y
    return False


if __name__ == '__main__':
    values = [line.strip() for line in open("input.txt")]
    nums, board_list = process_input()
    print(f"Part 1: " + str(part1()))
    print(f"Part 2: " + str(part2()))
