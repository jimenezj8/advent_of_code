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
    'x': 'lose',
    'b': 'paper',
    'y': 'tie',
    'c': 'scissors',
    'z': 'win',
}

win = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}
loss = {val: key for key, val in win.items()}

for round in data:
    opp, me = round.split(' ')
    opp = map[opp.lower()]
    me = map[me.lower()]

    match me:
        case 'tie':
            score += 3
            score += points[opp]

        case 'win':
            score += 6
            score += points[loss[opp]]

        case 'lose':
            score += points[win[opp]]

print(score)
