with open("./input.txt") as file:
    data = file.read()

chars = []
for i, char in enumerate(data):
    if char in chars:
        chars = chars[chars.index(char) + 1 :]
    chars.append(char)

    if len(chars) == 14:
        break

print(i + 1)
