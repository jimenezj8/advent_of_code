with open('/home/jimenezj/code/advent_of_code/2022/2/input.txt') as file:
    data = [round.strip() for round in file.readlines()]

score = 0

points = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

map = {
    'a': 'rock',
    'x': 'rock',
    'b': 'paper',
    'y': 'paper',
    'c': 'scissors',
    'z': 'scissors',
}

win = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

for round in data:
    opp, me = round.split(' ')
    opp = map[opp.lower()]
    me = map[me.lower()]

    score += points[me]

    if opp == me:
        score += 3

    elif win[me] == opp:
        score += 6


print(score)
