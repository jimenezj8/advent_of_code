import os

home_dir = os.getenv("HOME")
with open(f"{home_dir}/code/advent_of_code/2022/1/input.txt") as file:
    data = [
        [int(cals) for cals in elf.split("\n") if cals != ""]
        for elf in file.read().split("\n\n")
    ]

sums = [sum(items) for items in data]
sums.sort(reverse=True)
print(sums[0])
