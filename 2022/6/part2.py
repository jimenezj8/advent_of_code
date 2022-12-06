with open("./input.txt") as file:
    data = file.read()

unique = set()
order = []
for i, char in enumerate(data):
    if char in unique:
        order = order[order.index(char) + 1 :]
        unique.clear()
        unique = set(order)

    order.append(char)
    unique.add(char)

    if len(order) == 14:
        break

print(i + 1)
