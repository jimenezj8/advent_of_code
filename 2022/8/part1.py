import numpy as np


with open("./example.txt") as file:
    grid = [[int(i) for i in row.strip()] for row in file.readlines()]

visible = 0
grid_copy = []
for row in grid:
    row_copy = row
    forward = [tree > row[i - 1] if i != 0 else True for i, tree in enumerate(row_copy)]
    row_copy.reverse()
    reverse = [tree > row[i - 1] if i != 0 else True for i, tree in enumerate(row_copy)]

    print(np.array(forward))
    print(np.array(reverse))
