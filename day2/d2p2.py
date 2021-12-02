import re

with open('in.txt', 'r') as f:
    data = f.read()


data = data.splitlines()

horiz = 0
depth = 0
aim = 0

print('h, d, a')

for inst in data:
    num = int(inst[-1:])
    if inst.startswith('u'):
        aim -= num
    if inst.startswith('d'):
        aim += num
    if inst.startswith('f'):
        depth += aim*num
        horiz += num

    print(horiz, depth, aim)

print()
print(horiz, depth, aim, horiz*depth)

