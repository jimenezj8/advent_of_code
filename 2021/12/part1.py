with open("example1.txt") as file:
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


def explore(from_cave: str, no_return: list[str] = []) -> int | None:
    possible_paths = 0
    for next in paths[from_cave]:
        if next in no_return:
            return

    return possible_paths


possible_paths = 0
for cave in paths["start"]:
    possible_paths += explore(cave)
