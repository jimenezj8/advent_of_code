import numpy as np

filenames = {"e": "example", "i": "input"}
filename = filenames[
    input("Which file would you like to use? e for example and i for input: >")
]
with open(filename + ".txt") as file:
    risk_map = np.array(
        [[val for val in line.strip()] for line in file.readlines()], dtype=float
    )

chosen_risks = []
location = [0, 0]  # y, x to translate easier with numpy


def move_once(location: list[int]) -> list[int]:
    row_avg = np.sum(risk_map[location[0], location[1] :])
    col_avg = np.sum(risk_map[location[0] :, location[1]])

    new_location = location.copy()
    if row_avg > col_avg:
        new_location[1] += 1
    elif col_avg > row_avg:
        new_location[0] += 1
    else:
        print("fuck")

    return new_location


destination = [val - 1 for val in risk_map.shape]
while location != destination:
    try:
        location = move_once(location)
        chosen_risks.append(risk_map[location[0], location[1]])
    except IndexError:
        print(location)
        print(chosen_risks)
        print("fuck")
        raise

print(sum(chosen_risks))
