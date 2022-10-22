scoring = {")": 3, "]": 57, "}": 1197, ">": 25137}
chunk_chars = {"(": ")", "[": "]", "{": "}", "<": ">"}


def search_for_close(string):
    score = 0
    open_chars = []
    for index, char in enumerate(string):
        if char in chunk_chars.keys():
            open_chars.append(char)
        elif char in chunk_chars.values():
            if char != chunk_chars[open_chars[-1]]:
                score += scoring[char]
                return score
            else:
                open_chars.pop(-1)


with open("input.txt") as file:
    data = file.read().strip("\n").split("\n")

score = 0
for line in data:
    line_score = search_for_close(line)
    if not line_score:
        continue
    else:
        score += line_score

print(score)
