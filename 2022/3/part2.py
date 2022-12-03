with open('2022/3/input.txt') as file:
    sacks = [sack.strip() for sack in file.readlines()]

priority = 'abcdefghijklmnopqrstuvwxyz'
priority += priority.upper()

priorities = []
for i in range(len(sacks) // 3):
    group_sacks = sacks[3*i:3*i+3]
    sack1 = group_sacks[0]
    for item in sack1:
        if item in group_sacks[1] and item in group_sacks[2]:
            common = item
    priorities.append(priority.index(common)+1)

print(sum(priorities))
