import datetime

import pandas as pd
from common import Solution, get_neighbor

PATH = get_neighbor(__file__, "input.txt")


def solve():
    start = datetime.datetime.utcnow()
    part1 = _part1()
    part2 = _part2()
    runtime = datetime.datetime.utcnow() - start
    return Solution(3, part1, part2, runtime)


def _part1():
    return 0


def _part2():
    with open(PATH) as file:
        data = [val.strip("\n") for val in file]

    expanded = [[i for i in val] for val in data]

    df = pd.DataFrame(expanded)

    o = df.copy()
    c = df.copy()

    for col in df.columns:
        if len(o) > 1:
            filter = int(o[col].astype(int).sum() // (len(o) / 2))
            o = o.loc[
                (o[col] == str(filter)),
            ].copy()
        if len(c) > 1:
            filter = int(-((c[col].astype(int).sum() // (len(c) / 2)) - 1))
            c = c.loc[
                (c[col] == str(filter)),
            ].copy()

    o_rating = int("".join(o.iloc[0]), 2)
    c_rating = int("".join(c.iloc[0]), 2)

    final = o_rating * c_rating

    return final
