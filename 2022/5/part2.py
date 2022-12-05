with open("2022/5/input.txt") as file:
    crates_input, dirs = file.read().split("\n\n")

dirs = [dir for dir in dirs.split("\n") if dir != ""]

stacks = crates_input.split("\n")[-1]
crates = []
for text_pos, stack_num in enumerate(stacks):
    if stack_num != " ":
        stack_crates = [
            level[text_pos]
            for level in crates_input.split("\n")
            if level[text_pos] != " "
        ]
        stack_crates.pop(-1)
        crates.append(stack_crates)

for dir in dirs:
    instr = dir.split(" ")
    num_crates, start, end = int(instr[1]), int(instr[3]) - 1, int(instr[5]) - 1
    crates_moved = [crates[start].pop(0) for i in range(num_crates)]
    crates[end] = crates_moved + crates[end]

tops = [stack[0] for stack in crates]
tops = "".join(tops)
print(tops)
