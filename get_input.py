import os
import requests
import sys

from dotenv import load_dotenv


load_dotenv()
root = 'https://adventofcode.com'
project_root = '/'.join([os.getenv('HOME'), 'code/advent_of_code'])


def request_input(year: str, day: str) -> None:
    session = requests.Session()
    session.cookies.set('session', os.getenv('SESSION'))

    response = session.get('/'.join([root, year, 'day', day, 'input']))

    with open('/'.join([project_root, year, day, 'input.txt']), 'w') as file:
        file.write(response.text)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)

    pwd = os.getenv('PWD').split('/')
    pwd.reverse()
    day, year = pwd[0: 2]

    # request_input(year, day)

    print('Downloaded input.txt')
