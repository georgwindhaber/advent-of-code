file = open("input.txt", "r")
lines = file.readlines()

values = []
currentSum = 0

for line in lines:
    value = line.replace("\n", "")
    if (len(value)):
        currentSum = currentSum + int(value)
    else:
        values.append(currentSum)
        currentSum = 0

values.sort()

print(values[-1] + values[-2] + values[-3])
