import datetime

from common import Solution, get_neighbor

PATH = get_neighbor(__file__, "input.txt")


def solve():
    start = datetime.datetime.utcnow()
    part1 = _part1()
    part2 = _part2()
    runtime = datetime.datetime.utcnow() - start

    return Solution(6, part1, part2, runtime)


def _part1():
    with open(PATH) as file:
        data = [int(val) for val in file.read().strip("\n").split(",")]

    stats = {x: data.count(x) for x in range(9)}

    today = stats.copy()
    tomorrow = {}
    for i in range(80):
        if i != 0:
            today = tomorrow.copy()

        for j in range(9):
            if j == 8:
                tomorrow[j] = today[0]
            elif j == 6:
                tomorrow[j] = today[0] + today[j + 1]
            else:
                tomorrow[j] = today[j + 1]

    return sum(tomorrow.values())


def _part2():
    with open(PATH) as file:
        data = [int(val) for val in file.read().strip("\n").split(",")]

    stats = {x: data.count(x) for x in range(9)}

    today = stats.copy()
    tomorrow = {}
    for i in range(256):
        if i != 0:
            today = tomorrow.copy()

        for j in range(9):
            if j == 8:
                tomorrow[j] = today[0]
            elif j == 6:
                tomorrow[j] = today[0] + today[j + 1]
            else:
                tomorrow[j] = today[j + 1]

    return sum(tomorrow.values())
