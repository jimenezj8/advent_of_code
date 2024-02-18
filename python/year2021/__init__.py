"""Advent of Code 2021

This subpackage contains a subpackage for each day of the calendar.

In order to run all the solutions, use the top-level `solve` function.
"""

from . import (
    day03,
    day04,
    day05,
    day06,
    day07,
    day08,
    day09,
    day10,
    day11,
    day12,
    day13,
    day14,
    day15,
)


def solve():
    print(day03.solve())
    print(day04.solve())
    print(day05.solve())
    print(day06.solve())
    print(day07.solve())
    print(day08.solve())
    print(day09.solve())
    print(day10.solve())
    print(day11.solve())
    print(day12.solve())
    print(day13.solve())
    print(day14.solve())
    print(day15.solve())


if __name__ == "__main__":
    solve()
