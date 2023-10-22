import numpy as np
import pandas as pd

with open("input.txt") as file:
    data = [
        [
            [int(val) for val in line.split(",")]
            for line in row.strip("\n").split(" -> ")
        ]
        for row in file
    ]

max_y = 0
max_x = 0
considered_lines = []
for line in data:
    x1, y1, x2, y2 = *line[0], *line[1]
    try:
        slope = abs((y2 - y1) / (x2 - x1))
    except ZeroDivisionError:
        slope = 0
    if x1 == x2 or y1 == y2 or slope == 0 or slope == 1:
        considered_lines.append(line)
    else:
        continue

    if y1 > max_y:
        max_y = y1
    if y2 > max_y:
        max_y = y2
    if x1 > max_x:
        max_x = x1
    if x2 > max_x:
        max_x = x2

tracker = np.zeros(shape=(max_y + 1, max_x + 1))

for line in considered_lines:
    x1, y1, x2, y2 = *line[0], *line[1]

    if x1 == x2:
        if y1 > y2:
            for y in np.arange(y2, y1 + 1).tolist():
                tracker[int(y), x1] += 1
        else:
            for y in np.arange(y1, y2 + 1).tolist():
                tracker[int(y), x1] += 1
    elif y1 == y2:
        if x1 > x2:
            for x in np.arange(x2, x1 + 1).tolist():
                tracker[y1, int(x)] += 1
        else:
            for x in np.arange(x1, x2 + 1).tolist():
                tracker[y1, int(x)] += 1

    else:
        if x1 > x2:
            x_start, x_stop = x2, x1
            flip_x = True
        else:
            x_start, x_stop = x1, x2
            flip_x = False

        if y1 > y2:
            y_start, y_stop = y2, y1
            flip_y = True
        else:
            y_start, y_stop = y1, y2
            flip_y = False

        x_range = np.arange(x_start, x_stop + 1)
        y_range = np.arange(y_start, y_stop + 1)

        x_range = np.flip(x_range) if flip_x is True else x_range
        y_range = np.flip(y_range) if flip_y is True else y_range

        for index in range(len(x_range)):
            tracker[y_range[index], x_range[index]] += 1

print("Intersections:", np.sum(tracker >= 2))
