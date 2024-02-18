import datetime

from common import Solution, get_neighbor

PATH = get_neighbor(__file__, "input.txt")


def solve():
    start = datetime.datetime.utcnow()
    part1 = _part1()
    part2 = _part2()
    runtime = datetime.datetime.utcnow() - start

    return Solution(4, part1, part2, runtime)


def _part1():
    boards = []
    with open(PATH) as file:
        current_board = []
        for i, row in enumerate(file):
            if not i:
                numbers = [int(val.strip("\n")) for val in row.split(",")]
            elif row != "\n":
                current_row = [
                    int(val.strip("\n")) for val in row.split(" ") if val != ""
                ]
                current_board.append(current_row)
            else:
                if current_board != []:
                    boards.append(current_board)
                current_board = []

    board_dicts = {
        b: {
            "rows": {x: [] for x in range(5)},
            "cols": {x: [] for x in range(5)},
        }
        for b in range(len(boards))
    }

    def pick_numbers(numbers):
        for num in numbers:
            for board_num, board in enumerate(boards):
                for row_num, row in enumerate(board):
                    for col_num, value in enumerate(row):
                        if value == num:
                            board_dicts[board_num]["rows"][row_num].append(value)
                            board_dicts[board_num]["cols"][col_num].append(value)

                            if len(board_dicts[board_num]["rows"][row_num]) == 5:
                                # print(f"Board #{board_num} wins")
                                return board_num, value

                            if len(board_dicts[board_num]["cols"][col_num]) == 5:
                                # print(f"Board #{board_num} wins")
                                return board_num, value

    winning_board, final_val = pick_numbers(numbers)

    marked_total = sum(
        [sum(row) for row in board_dicts[winning_board]["rows"].values()]
    )

    board_total = sum([sum(row) for row in boards[winning_board]])

    unmarked_total = board_total - marked_total

    board_score = unmarked_total * final_val

    return board_score


def _part2():
    boards = []
    with open(PATH) as file:
        current_board = []
        for i, row in enumerate(file):
            if not i:
                numbers = [int(val.strip("\n")) for val in row.split(",")]
            elif row != "\n":
                current_row = [
                    int(val.strip("\n")) for val in row.split(" ") if val != ""
                ]
                current_board.append(current_row)
            else:
                if current_board != []:
                    boards.append(current_board)
                current_board = []

    board_dicts = {
        b: {
            "rows": {x: [] for x in range(5)},
            "cols": {x: [] for x in range(5)},
        }
        for b in range(len(boards))
    }
    incomplete_boards = [board_num for board_num, board in enumerate(boards)]

    def pick_numbers(numbers):
        for num in numbers:
            for board_num, board in enumerate(boards):
                for row_num, row in enumerate(board):
                    for col_num, value in enumerate(row):
                        if value == num:
                            board_dicts[board_num]["rows"][row_num].append(value)
                            board_dicts[board_num]["cols"][col_num].append(value)

                            if len(board_dicts[board_num]["rows"][row_num]) == 5:
                                if board_num not in incomplete_boards:
                                    continue
                                # print(f"Board #{board_num} wins with row {row_num}")
                                incomplete_boards.remove(board_num)
                                if len(incomplete_boards) == 0:
                                    return board_num, value

                            if len(board_dicts[board_num]["cols"][col_num]) == 5:
                                if board_num not in incomplete_boards:
                                    continue
                                # print(f"Board #{board_num} wins with column {col_num}")
                                incomplete_boards.remove(board_num)
                                if len(incomplete_boards) == 0:
                                    return board_num, value

    winning_board, final_val = pick_numbers(numbers)

    marked_total = sum(
        [sum(row) for row in board_dicts[winning_board]["rows"].values()]
    )

    board_total = sum([sum(row) for row in boards[winning_board]])

    unmarked_total = board_total - marked_total

    board_score = unmarked_total * final_val

    return board_score
