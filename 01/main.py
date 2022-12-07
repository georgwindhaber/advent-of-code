file = open("input.txt", "r")
lines = file.readlines()

max = 0
currentSum = 0

for line in lines:
    value = line.replace("\n", "")
    if (len(value)):
        currentSum = currentSum + int(value)
    else:
        if (currentSum > max):
            max = currentSum
        currentSum = 0

print(max)
