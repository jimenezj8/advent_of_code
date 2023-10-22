import numpy as np

filenames = {"e": "example", "i": "input"}
filename = filenames[
    input("Which file would you like to use? e for example and i for input: >")
]
with open(filename + ".txt") as file:
    coords, folds = file.read().split("\n\n")
    coords = [[int(val) for val in pair.split(",")] for pair in coords.split()]
    folds = [fold.split(" ")[-1] for fold in folds.split("\n") if fold != ""]

max_x, max_y = None, None
for fold in folds:
    if "x" in fold and not max_x:
        max_x = int(fold.split("=")[-1]) * 2 + 1
    elif "y" in fold and not max_y:
        max_y = int(fold.split("=")[-1]) * 2 + 1
grid = np.zeros((max_y, max_x), bool)

for x, y in coords:
    grid[y, x] = True

for i, fold in enumerate(folds):
    axis, point = fold.split("=")
    point = int(point)
    if axis == "y":
        half1 = grid[0:point, :]
        half2 = grid[point + 1 :, :]
        rows = []
        for row in half2:
            rows.append(row)
        rows.reverse()
        half2 = np.array(rows)

    elif axis == "x":
        half1 = grid[:, 0:point]
        half2 = grid[:, point + 1 :]
        rows = []
        for row in half2:
            vals = [val for val in row]
            vals.reverse()
            rows.append(vals)
        half2 = np.array(rows)

    grid = half1 | half2
    dots = np.sum(grid)
    print(f"Dots visible after {i + 1} folds: {dots}")
