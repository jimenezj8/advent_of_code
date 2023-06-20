import datetime

import common

common.init()

path = "2022/1/input.txt"


def solve() -> int:
    start = datetime.datetime.utcnow()

    data = common.load_input(path)
    part_one = part_one(data)
    part_two = part_two(data)

    runtime = datetime.datetime.utcnow() - start

    return common.Solution(1, part_one, part_two, runtime)


def part_one(data: str) -> int:
    data = [
        [int(cals) for cals in elf.split("\n") if cals != ""]
        for elf in data.split("\n\n")
    ]
    sums = [sum(items) for items in data]
    sums.sort(reverse=True)
    return sums[0]


def part_two(data: str) -> int:
    data = [
        [int(cals) for cals in elf.split("\n") if cals != ""]
        for elf in data.read().split("\n\n")
    ]
    sums = [sum(items) for items in data]
    sums.sort(reverse=True)
    return sum(sums[:3])
