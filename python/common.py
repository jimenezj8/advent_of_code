import datetime

import dotenv


def init():
    "Initializes the environment based on the specified config"
    dotenv.load_dotenv()


def load_input(path: str) -> str:
    "Reads the input file at path into a string"
    with open(path) as file:
        return file.read()


class Solution:
    "Utility class representing the solutions for an Advent of Code puzzle"

    def __init__(self, day: int, part_one, part_two, runtime: datetime.timedelta):
        self.day = day
        self.part_one = part_one
        self.part_two = part_two
        self.runtime = runtime

    def __repr__(self):
        return f"Day: {self.day}, Part One: {self.part_one}, Part Two: {self.part_two}, Runtime: {self.runtime}"
