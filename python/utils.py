"Advent of Code project meta utilities"

import logging
import os

import requests
from dotenv import load_dotenv

from python.common import get_parent_path

URL_ROOT = "https://adventofcode.com"
PROJECT_ROOT = get_parent_path(__file__)

logger = logging.getLogger(__name__)


def init(year: int, day: int):
    """Initialize a solution space for an Advent of Code calendar day.

    Sets up a directory with the required input file and a solution template
    to fill in.
    """
    load_dotenv()

    create_template_dir(year, day)

    load_input(year, day)


def copy_solution_template(dest: str):
    with open("/".join([PROJECT_ROOT, "template.py"])) as file:
        template = file.read()

    with open("/".join([dest, "main.py"]), "w") as file:
        file.write(template)


def create_template_dir(year: int, day: int) -> str:
    """Creates a solution template directory and returns the path"""
    path = "/".join([PROJECT_ROOT, f"year{year}", f"day{day:0>2}"])

    os.mkdir(path)

    with open("/".join([path, "__init__.py"]), "w") as file:
        file.write("from .main import solve  # noqa")

    copy_solution_template(path)


def load_input(year: int, day: int) -> None:
    session = requests.Session()
    session.cookies.set("session", os.getenv("SESSION"))

    response = session.get("/".join([URL_ROOT, year, "day", day, "input"]))

    with open("/".join([PROJECT_ROOT, year, day, "input.txt"]), "w") as file:
        file.write(response.text)
