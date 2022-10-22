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


with open("input.txt") as file:
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


def search(starting_point: tuple[int, int], exclude: set[tuple[int]] = set()) -> int:
    size = 1
    row, col = starting_point
    exclude.add(starting_point)
    for dir in ["left", "right", "down", "up"]:
        match dir:
            case "left":
                shift_val = -1
                axis = 1
            case "right":
                shift_val = 1
                axis = 1
            case "down":
                shift_val = 1
                axis = 0
            case "up":
                shift_val = -1
                axis = 0

        next_row, next_col = (row + (shift_val * axis)), (
            col + (shift_val * (1 - axis))
        )
        if (next_row, next_col) in exclude:
            continue

        elif next_row >= data.shape[0] or next_col >= data.shape[1]:
            exclude.add((next_row, next_col))
            continue

        elif next_row < 0 or next_col < 0:
            exclude.add((next_row, next_col))
            continue

        elif data[next_row, next_col] < 9:
            size += search((next_row, next_col), exclude)

    return size


sizes = []
for row, values in enumerate(solution):
    for col, value in enumerate(values):
        if value:
            size = 0

            size += search((row, col))

            if len(sizes) < 3:
                sizes.append(size)
                sizes.sort(reverse=True)
            elif size > sizes[-1]:
                sizes.pop(-1)
                sizes.append(size)
                sizes.sort(reverse=True)

result = 1
for val in sizes:
    result = result * val

print(f"The 3 largest basins have sizes {sizes}, coming out to a product of {result}")
