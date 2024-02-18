filenames = {"e": "example", "i": "input"}
filename = filenames[
    input("Which file would you like to use? e for example and i for input: >")
]
with open(filename + ".txt") as file:
    template, rules = file.read().strip().split("\n\n")

rules = {
    pair: result for pair, result in [rule.split(" -> ") for rule in rules.split("\n")]
}

pair_counts = {rule: 0 for rule in rules.keys()}
for i in range(len(template) - 1):
    pair_counts[template[i] + template[i + 1]] += 1


def step(stats: dict[str, int]) -> dict[str, int]:
    new_stats = {pair: 0 for pair in rules.keys()}
    for pair, count in stats.items():
        first, second = pair
        new = rules[pair]

        first_pair = first + new
        second_pair = new + second

        new_stats[first_pair] += count
        new_stats[second_pair] += count

    return new_stats


for i in range(40):
    pair_counts = step(pair_counts)


chars = set("".join(pair_counts.keys()))
counts = {char: 0 for char in chars}
for pair, count in pair_counts.items():
    counts[pair[0]] += count

counts[template[-1]] += 1

print(
    f"Difference in counts between most frequent and least frequent characters: {max(counts.values()) - min(counts.values())}"
)
