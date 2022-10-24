filenames = {"e": "example", "i": "input"}
filename = filenames[
    input("Which file would you like to use? e for example and i for input: >")
]
with open(filename + ".txt") as file:
    template, rules = file.read().strip().split("\n\n")

rules = {
    pair: result for pair, result in [rule.split(" -> ") for rule in rules.split("\n")]
}

pair_counts = {}
for i in range(len(template) - 1):
    pair_counts[template[i] + template[i + 1]] = 1


def step(stats: dict[str:int]) -> str:
    new_stats = {}
    for pair, count in stats.items():
        first, second = pair
        new = rules[pair]

        first_pair = first + new
        second_pair = new + second

        if not new_stats.get(first_pair):
            new_stats[first_pair] = 0
        if not new_stats.get(second_pair):
            new_stats[second_pair] = 0

        new_stats[first_pair] += count
        new_stats[second_pair] += count

    return new_stats


for i in range(1):
    pair_counts = step(pair_counts)


chars = set("".join(pair_counts.keys()))
counts = {char: 0 for char in chars}
for char in chars:
    counts[char] += (
        sum([pair_counts[key] for key in pair_counts.keys() if char in key]) // 2 + 1
    )
    # for pair in pair_counts.keys():
    #     if char in pair:
    #         counts[char] += pair_counts[pair]

    # counts[char] = int(counts[char] // 2)

print(sum(counts.values()) + 1)
print(
    f"Difference in counts between most frequent and least frequent characters: {max(counts.values()) - min(counts.values())}"
)
