filenames = {"e": "example", "i": "input"}
filename = filenames[
    input("Which file would you like to use? e for example and i for input: >")
]
with open(filename + ".txt") as file:
    template, rules = file.read().strip().split("\n\n")

template = [char for char in template]
rules = {
    pair: result for pair, result in [rule.split(" -> ") for rule in rules.split("\n")]
}


def step(polymer: list) -> str:
    inserts = {}
    for i in range(len(polymer) - 1):
        first = polymer[i]
        second = polymer[i + 1]
        inserts[2 * i + 1] = rules[first + second]

    new_polymer = []
    for i in range(len(polymer)):
        new_polymer.append(polymer[i])
        new = inserts.get(2 * i + 1)
        if new:
            new_polymer.append(new)
    return new_polymer


for i in range(10):
    template = step(template)

chars = set(template)
counts = {char: template.count(char) for char in chars}
print(
    f"Difference in counts between most frequent and least frequent characters: {max(counts.values()) - min(counts.values())}"
)
