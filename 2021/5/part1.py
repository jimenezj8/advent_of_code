import numpy as np
import pandas as pd

with open('input.txt') as file:
    data = [[[int(val) for val in line.split(',')] for line in row.strip('\n').split(' -> ')] for row in file]

max_y = 0
max_x = 0
straight_lines = []
for line in data:
    x1, y1, x2, y2 = *line[0], *line[1]
    if x1 != x2 and y1 != y2:
        continue
    else:
        straight_lines.append(line)

    if y1 > max_y:
        max_y = y1
    if y2 > max_y:
        max_y = y2
    if x1 > max_x:
        max_x = x1
    if x2 > max_x:
        max_x = x2

tracker = np.zeros(shape=(max_y + 1, max_x + 1))

for line in straight_lines:
    x1, y1, x2, y2 = *line[0], *line[1]

    if x1 == x2:
        if y1 > y2:
            for y in np.arange(y2, y1 + 1).tolist():
                tracker[int(y), x1] += 1
        else:
            for y in np.arange(y1, y2 + 1).tolist():
                tracker[int(y), x1] += 1
    else:
        if x1 > x2:
            for x in np.arange(x2, x1 + 1).tolist():
                tracker[y1, int(x)] += 1
        else:
            for x in np.arange(x1, x2 + 1).tolist():
                tracker[y1, int(x)] += 1

print('Intersections:', np.sum(tracker >= 2))
