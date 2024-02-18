with open('2022/3/input.txt') as file:
    sacks = [sack.strip() for sack in file.readlines()]

priority = 'abcdefghijklmnopqrstuvwxyz'
priority += priority.upper()

priorities = []
for sack in sacks:
    comp1, comp2 = sack[:len(sack)//2], sack[len(sack)//2::]
    for item in comp1:
        if item in comp2:
            common = item

    priorities.append(priority.index(common)+1)

print(sum(priorities))
