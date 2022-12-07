with open("./input.txt") as file:
    hist = file.read()


def build_tree(shell_history: str) -> dict:
    tree = {}

    commands = shell_history.split("\n$")
    pwd = ""
    for command in commands:
        input, *output = command.splitlines()

        if input.strip().startswith("ls"):
            tree[pwd] = []
            for child in output:
                if child.startswith("dir"):
                    child_name = child.split()[1]
                    tree[pwd].append("/".join([pwd, child_name]))
                else:
                    filesize, filename = child.split()
                    tree[pwd].append((filename, filesize))

        elif input.startswith("$ cd"):
            continue
        else:
            next_dir = input.split()[1]
            if next_dir == "..":
                path = pwd.split("/")
                path.pop(-1)
                pwd = "/".join(path)
            else:
                pwd = "/".join([pwd, next_dir])

    return tree


def get_dirsize(dir: str, filesystem: dict, dirsizes: dict):
    children = filesystem[dir]

    size = 0

    for child in children:
        if isinstance(child, str):
            if child in dirsizes.keys():
                size += dirsizes[child]
            else:
                child_size, dirsizes = get_dirsize(child, filesystem, dirsizes)
                dirsizes[child] = child_size
                size += child_size
        else:
            size += int(child[1])

    return size, dirsizes


tree = build_tree(hist)

dirsizes = {}
for dir in tree.keys():
    dirsizes[dir], dirsizes = get_dirsize(dir, tree, dirsizes)

total = sum([size for dir, size in dirsizes.items() if size <= 100000])

print(total)
