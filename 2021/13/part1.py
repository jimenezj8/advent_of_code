filenames = {"e": "example", "i": "input"}
filename = filenames[
    input("Which file would you like to use? e for example and i for input: >")
]
with open(filename + ".txt") as file:
    coords, folds = file.read().split("\n\n")
    coords = [pair.split(",") for pair in coords]
