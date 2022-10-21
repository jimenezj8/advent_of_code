with open("example1.txt") as file:
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

def filter_clues(number: int, characters: set[str], clues: dict[int, set[str]]):
    keep = mapping[number]
    toss = positions.difference(keep)

    return_clues = clues.copy()
    for position in keep:
        return_clues[position].intersection_update(characters)
    for position in toss:
        return_clues[position].difference_update(characters)

    return return_clues

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

    all_sequences = signals + output
    lengths = [len(val) for val in all_sequences]

    # 0, 6, 9 will all have len 6 and would be missing mid, top right, and bottom left
    # 1 has len 2 and has both right pieces
    # 2, 3, 5 all have len 5 and missing top right + bottom left, both left, and top right + bottom left
    # 4 has len 4
    # 7 has len 3
    # 8 has len 7 and provides no information to us

    unique = [all_sequences[index] for index, length in enumerate(lengths) if length in [2, 3, 4]]

    # first we filter the unique ones that give the most information

    clues = {loc: set(["a", "b", "c", "d", "e", "f", "g"]) for loc in positions}
    for sequence, char_count in zip(unique, [len(string) for string in unique]):
        try:
            match char_count:
                case 2:
                    key = 1
                case 3:
                    key = 7
                case 4:
                    key = 4
                case _:
                    continue
            clues = filter_clues(key, set([char for char in sequence]), clues)
        except ValueError:
            continue

    potential_solution = clues.copy()
    print(potential_solution)
    for sequence, num_chars in zip(all_sequences, lengths):
        if num_chars == 5:
            for key in [2, 3, 5]:
                next_attempt = filter_clues(key, set([char for char in sequence]), potential_solution)

                if all([len(possibilities) == 1 for possibilities in next_attempt.values()]):
                    potential_solution = next_attempt.copy()
                    break

                elif set() not in next_attempt.values():
                    potential_solution = next_attempt.copy()

        elif num_chars == 6:
            for key in [0, 6, 9]:
                next_attempt = filter_clues(key, set([char for char in sequence]), potential_solution)

                if all([len(possibilities) == 1 for possibilities in next_attempt.values()]):
                    potential_solution = next_attempt.copy()
                    break

                elif set() not in next_attempt.values():
                    potential_solution = next_attempt.copy()

        else:
            continue

        if all([len(possibilities) == 1 for possibilities in potential_solution.values()]):
            break

print(potential_solution)


print(f"The sum of the output is {total}")
