with open("input.txt") as file:
    data = [line.split(" | ") for line in file.read().split("\n") if line != ""]

count = 0
looking_for = [2, 3, 4, 7]
for line in data:
    for digit in line[1].split(" "):
        if len(digit) in looking_for:
            count += 1

print(count)
