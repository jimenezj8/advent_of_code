with open("example1.txt") as file:
    data = [line.split(" | ") for line in file.read().split("\n") if line != ""]

segments = {"a", "b", "c", "d", "e", "f", "g"}
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


def check_all_unique(sequences: list[int]) -> bool:
    lengths = [len(seq) for seq in sequences]
    if set(lengths).issubset({2, 3, 4, 7}):
        return True

    return False


def get_unique_val(sequence: str) -> str:
    match len(sequence):
        case 2:
            return "1"
        case 3:
            return "7"
        case 4:
            return "4"
        case 7:
            return "8"


def get_clues_from_unique(sequences: list[str]) -> dict[str, set[str]]:
    lengths = [len(seq) for seq in sequences]
    unique = [
        sequences[index] for index, length in enumerate(lengths) if length in [2, 3, 4]
    ]

    clues = {loc: segments.copy() for loc in positions}
    for seq in unique:
        key = int(get_unique_val(seq))
        clues = filter_clues(key, set([char for char in seq]), clues)

    return clues


total = 0
for entry in data:
    signals = entry[0].split(" ")
    output = entry[1].split(" ")

    if check_all_unique(output):
        value = ""
        for sequence in output:
            value.append(get_unique_val(sequence))
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

    # first we create a solution space with the sequences that have unique lengths
    potential_solution = get_clues_from_unique(all_sequences)

    # then we attempt to use the remaining sequences to narrow the solution
    for sequence, num_chars in zip(all_sequences, lengths):
        print("here")
        if num_chars == 5:
            for key in [2, 3, 5]:
                next_attempt = filter_clues(
                    key, set([char for char in sequence]), potential_solution
                )

                if all(
                    [len(possibilities) == 1 for possibilities in next_attempt.values()]
                ):
                    print("here")
                    potential_solution = next_attempt.copy()
                    break

                elif set() not in next_attempt.values():
                    print("here2")
                    potential_solution = next_attempt.copy()

        elif num_chars == 6:
            for key in [0, 6, 9]:
                next_attempt = filter_clues(
                    key, set([char for char in sequence]), potential_solution
                )

                if all(
                    [len(possibilities) == 1 for possibilities in next_attempt.values()]
                ):
                    print("here")
                    potential_solution = next_attempt.copy()
                    break

                elif set() not in next_attempt.values():
                    print("here2")
                    potential_solution = next_attempt.copy()

        else:
            continue

        if all(
            [len(possibilities) == 1 for possibilities in potential_solution.values()]
        ):
            break

print(potential_solution)


print(f"The sum of the output is {total}")
