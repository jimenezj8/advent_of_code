import numpy as np

with open("input.txt") as file:
    data = [[char for char in line] for line in file.read().strip("\n").split("\n")]

data = np.array(data, float)
solution = np.ndarray(data.shape, bool)
solution[:] = True

move_right = np.roll(data, 1)
move_right[:, 0] = 10
solution = solution & (data < move_right)

move_left = np.roll(data, -1)
move_left[:, -1] = 10
solution = solution & (data < move_left)

move_down = np.roll(data, 1, 0)
move_down[0, :] = 10
solution = solution & (data < move_down)

move_up = np.roll(data, -1, 0)
move_up[-1, :] = 10
solution = solution & (data < move_up)

risk = data + 1

total_risk = np.sum(solution * risk)
print(total_risk)
