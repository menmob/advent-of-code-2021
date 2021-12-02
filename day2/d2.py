import re

with open('in.txt', 'r') as f:
    data = f.read()


data = data.splitlines()

horiz = 0
depth = 0

for inst in data:
    num = int(inst[-1:])
    if inst.startswith('u'):
        depth -= num
    if inst.startswith('d'):
        depth += num
    if inst.startswith('f'):
        horiz += num

print(horiz, depth, horiz*depth)

