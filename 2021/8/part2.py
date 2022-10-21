with open("input.txt") as file:
    data = [line.split(" | ") for line in file.read().split("\n") if line != ""]

positions = {"t", "tr", "tl", "m", "br", "bl", "b"}
mapping = {
    0: positions.difference({"m"}),
    1: {"tr", "br"},
    2: positions.difference({"tl", "br"}),
    3: positions.difference({"tl", "bl"}),
    4: positions.difference({"t", "bl", "b"}),
    5: positions.difference({"tr", "bl"}),
    6: positions.difference({"tr"}),
    7: {"t", "tr", "br"},
    8: positions.copy(),
    9: positions.difference({"bl"}),
}

total = 0
for entry in data:
    signals = entry[0].split(" ")
    output = entry[1].split(" ")

    output_lengths = [len(val) for val in output]
    if set(output_lengths).issubset({2, 3, 4, 7}):
        value = ""
        for val in output:
            match len(val):
                case 2:
                    value += "1"
                case 3:
                    value += "7"
                case 4:
                    value += "4"
                case 7:
                    value += "8"
        total += int(value)
        continue

    all = signals + output

    lengths = [len(val) for val in all]

    # 0, 6, 9 will all have len 6 and would be missing mid, top right, and bottom left
    # 1 has len 2 and has both right pieces
    # 2, 3, 5 all have len 5 and missing top right + bottom left, both left, and top right + bottom left
    # 4 has len 4
    # 7 has len 3
    # 8 has len 7

    clues = {loc: set(["a", "b", "c", "d", "e", "f", "g"]) for loc in positions}
    for char_count in [2, 3, 4]:
        try:
            chars = set([char for char in all[lengths.index(char_count)]])
            match char_count:
                case 2:
                    key = 1
                case 3:
                    key = 7
                case 4:
                    key = 4
                case _:
                    continue
            keep = mapping[key]
            toss = positions.difference(keep)

            for pos in keep:
                clues[pos].intersection_update(chars)
            for pos in toss:
                clues[pos].difference_update(chars)
        except ValueError:
            continue

    length5 = [2, 3, 5]
    length6 = [0, 6, 9]
    # TODO: find how to discern which len(5) values correspond to which number


print(f"The sum of the output is {total}")
