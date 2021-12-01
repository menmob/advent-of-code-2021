
with open('day1in', 'r') as f:
    data = f.read()


data = data.splitlines()



count = 0
sum = 99999999999
for i in range(0,len(data)-2):
    if sum < int(int(data[i]) + int(data[i+1]) + int(data[i+2])):
        count += 1
        print(sum, int(int(data[i]) + int(data[i+1]) + int(data[i+2])))
    sum = int(data[i]) + int(data[i+1]) + int(data[i+2])

print(count)


