with open("input.txt") as file:
    data = [path.split("-") for path in file.read().strip().split()]

paths: dict[str, set[str]] = {}
for start, end in data:
    if start in paths.keys():
        paths[start].add(end)
    else:
        paths[start] = {end}

    if end == "end" or start == "start":
        continue

    if end in paths.keys():
        paths[end].add(start)
    else:
        paths[end] = {start}


def explore(
    from_cave: str, no_return: set[str] = set(), second_visit: bool = False
) -> int:
    possible_paths = 0
    if from_cave.islower():
        no_return.add(from_cave)

    for next in paths[from_cave]:
        if next == "end":
            possible_paths += 1

        elif next == "start":
            continue

        elif next in no_return:
            if not second_visit:
                possible_paths += explore(next, no_return.copy(), True)
            continue

        else:
            possible_paths += explore(next, no_return.copy(), second_visit)

    return possible_paths


possible_paths = explore("start")
print(f"Possible paths from start to end: {possible_paths}")
