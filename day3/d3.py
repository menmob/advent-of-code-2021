with open('in.txt', 'r') as f:
    data = f.read().splitlines()
    f.close()


ones = [0] * 12
zeros = [0] * 12


epsilon = ""
gamma = ""



for num in data:
    for i in range(0,12):
        if int(num[i]) == 0: zeros[i] += 1
        if int(num[i]) == 1: ones[i] += 1


print(str(ones))
print(str(zeros))


for i in range(0,12):
    if ones[i] > zeros[i]: epsilon += "1"
    else: epsilon += "0"
print(epsilon)


for i in range(0,12):
    if ones[i] < zeros[i]: gamma += "1"
    else: gamma += "0"
print(gamma)

