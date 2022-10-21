with open('input.txt') as file:
    data = [int(val) for val in file.read().strip('\n').split(',')]

stats = {
    x: data.count(x)
    for x in range(9)
}

today = stats.copy()
tomorrow = {}
for i in range(256):
    if i != 0:
        today = tomorrow.copy()

    for j in range(9):
        if j == 8:
            tomorrow[j] = today[0]
        elif j == 6:
            tomorrow[j] = today[0] + today[j + 1]
        else:
            tomorrow[j] = today[j + 1]

print(sum(tomorrow.values()))
