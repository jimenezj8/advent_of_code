import numpy as np


def shift(array, spots, axis=1, fill_val=10):
    shifted = np.roll(array, spots, axis)
    if spots > 0:
        if axis:
            shifted[:, 0:spots] = fill_val
        else:
            shifted[0:spots, :] = fill_val
    else:
        if axis:
            shifted[:, spots:] = fill_val
        else:
            shifted[spots:, :] = fill_val

    return shifted


with open("example.txt") as file:
    data = [[char for char in line] for line in file.read().strip("\n").split("\n")]

data = np.array(data, float)
solution = np.ndarray(data.shape, bool)
solution[:] = True

move_right = shift(data, 1)
solution = solution & (data < move_right)

move_left = shift(data, -1)
solution = solution & (data < move_left)

move_down = shift(data, 1, 0)
solution = solution & (data < move_down)

move_up = shift(data, -1, 0)
solution = solution & (data < move_up)

# at this point we have all the lowest points
# so we just need to find all connecting points
# that are not 9
# guess we can brute force with a loop?


def search(starting_point):
    for dir in ["left", "right", "down", "up"]:
        done = False
        match dir:
            case "left":
                multiplier = -1
                axis = 1
                limit = col
            case "right":
                multiplier = 1
                axis = 1
                limit = data.shape[1] - 1 - col
            case "down":
                multiplier = 1
                axis = 0
                limit = data.shape[0] - 1 - row
            case "up":
                multiplier = -1
                axis = 0
                limit = row
        steps = 1
        while not done:
            if steps == limit:
                done = True
            elif shift(data, steps * multiplier, axis)[row, col] < 9:
                size += 1
                steps += 1
            else:
                done = True


sizes = []
for row, values in enumerate(solution):
    for col, value in enumerate(values):
        if value:
            size = 1  # every basin is at least size 1

            print(sizes)
            if len(sizes) < 3:
                sizes.append(size)
                sizes.sort(reverse=True)
            elif size > sizes[0]:
                sizes.pop(0)
                sizes.append(size)
                sizes.sort(reverse=True)

result = 1
for val in sizes:
    result = result * val

print(result)
