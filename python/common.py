"Advent of Code utilities that are common to all puzzles"

import datetime


def get_parent_path(filepath: str) -> str:
    return "/".join(filepath.split("/")[:-1])


def get_neighbor(filepath: str, neighbor: str) -> str:
    parent_path = get_parent_path(filepath)
    return "/".join(parent_path.split("/") + [neighbor])


class Solution:
    "Utility class representing a solution for an Advent of Code puzzle"

    def __init__(self, day: int, part_one, part_two, runtime: datetime.timedelta):
        self.day = day
        self.part_one = part_one
        self.part_two = part_two
        self.runtime = runtime

    def __repr__(self):
        return f"Day: {self.day:>02}, Part One: {self.part_one:>02}, Part Two: {self.part_two}, Runtime: {self.runtime}"
