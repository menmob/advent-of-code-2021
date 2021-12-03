with open('in.txt', 'r') as f:
    data = f.read().splitlines()
    f.close()


ones = 0
zeros = 0


oxygen = None
for i in range(0,12):
    ones = 0
    zeros = 0
    print(i)
    if len(data) == 1:
        break
    for num in data:
        if int(num[i]) == 0: zeros += 1
        if int(num[i]) == 1: ones += 1

    j = 0
    while True:
        if j >= len(data): break
        if (data[j][i] == "1" and zeros < ones): 
            data.pop(j)
            j -=1 
        elif (data[j][i] == "0" and zeros > ones): 
            data.pop(j)
            j -= 1
        elif (data[j][i] == "1" and zeros == ones): 
            data.pop(j)
            j -= 1
        j +=1





print(str(data))

#oxygen == 1679
#c02 = 3648

