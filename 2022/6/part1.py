with open("./input.txt") as file:
    data = file.read()

unique = set()
for i, char in enumerate(data):
    if char in unique:
        unique.clear()
    unique.add(char)

    if len(unique) == 4:
        break

print(i + 1)
