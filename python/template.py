import datetime

from python.common import Solution, get_neighbor

PATH = get_neighbor(__file__, "input.txt")


def solve():
    start = datetime.datetime.utcnow()
    part1 = _part1()
    part2 = _part2()
    runtime = datetime.datetime.utcnow() - start

    return Solution(int(PATH.split("/")[-2]), part1, part2, runtime)


def _part1():
    pass


def _part2():
    pass
