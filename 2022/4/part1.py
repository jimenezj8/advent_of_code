with open('./input.txt') as file:
    pairs = [line.strip().split(',') for line in file.readlines()]


contained = 0

for pair in pairs:
    first, second = pair

    first = {i for i in range(int(first.split('-')[0]), int(first.split('-')[1]) + 1, 1)}
    second = {i for i in range(int(second.split('-')[0]), int(second.split('-')[1]) + 1, 1)}

    if first.issuperset(second) or second.issuperset(first):
        contained += 1

print(contained)
