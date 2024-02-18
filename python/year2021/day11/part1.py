import numpy as np

with open("input.txt") as file:
    data = [[val for val in line] for line in file.read().strip("\n").split("\n")]

energy = np.array(data, float)


def increment_surrounding(
    origin: tuple[int, int], cant_flash: set[tuple[int, int]] = set()
) -> int:
    cant_flash.add(origin)
    row, col = origin
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            next_row = row + i
            next_col = col + j
            if (
                next_row < 0
                or next_col < 0
                or next_row >= energy.shape[0]
                or next_col >= energy.shape[1]
                or (next_row, next_col) == origin
            ):
                continue

            energy[next_row, next_col] += 1

            if (next_row, next_col) in cant_flash:
                continue

            if energy[next_row, next_col] > 9:
                increment_surrounding((next_row, next_col), cant_flash)


total_flashes = 0
for step in range(100):
    energy += 1
    cant_flash = set()
    for row, row_vals in enumerate(energy):
        for col, octopus in enumerate(row_vals):
            if (row, col) in cant_flash:
                continue
            elif energy[row, col] > 9:
                increment_surrounding((row, col), cant_flash)

    flashed = energy > 9
    total_flashes += np.sum(flashed)
    energy = energy * ~flashed

print(f"Total octopus flashes: {total_flashes}")
