scoring = {")": 1, "]": 2, "}": 3, ">": 4}
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
                return
            else:
                open_chars.pop(-1)
    open_chars.reverse()
    for char in open_chars:
        score = score * 5
        score += scoring[chunk_chars[char]]

    return score


with open("input.txt") as file:
    data = file.read().strip("\n").split("\n")

scores = []
for line in data:
    line_score = search_for_close(line)
    if not line_score:
        continue
    else:
        scores.append(line_score)

scores.sort()

print(scores[int(round(len(scores) / 2, 0))])
