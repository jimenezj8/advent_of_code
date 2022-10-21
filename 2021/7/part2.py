with open('input.txt') as file:
    data = [int(val) for val in file.read().strip('\n').split(',')]


position_stats = {pos: 0 for pos in set(data)}
for pos in position_stats.keys():
    position_stats[pos] = data.count(pos)

positions = range(max(position_stats.keys()) + 1)

def calc_fuel_use(current, final):
    steps = abs(current - final)
    total_fuel = 0
    for i in range(steps):
        total_fuel += (steps - i)
    return total_fuel

min_fuel_req = None
min_fuel_pos = None
for pos in positions:
    fuel_req = sum([calc_fuel_use(val, pos) for val in data])
    if min_fuel_req is not None and fuel_req < min_fuel_req:
        min_fuel_req = fuel_req
        min_fuel_pos = pos
    elif min_fuel_req is None:
        min_fuel_req = fuel_req
        min_fuel_pos = pos

print(min_fuel_req)
print(min_fuel_pos)
