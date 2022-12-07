file = open("input.txt", "r")
lines = file.readlines()

sum = 0

for line in lines:
    rawLine = line.replace("\n", "")
    first = rawLine[0:int(len(rawLine) / 2)]
    last = rawLine[int(len(rawLine) / 2):]

    for character in first:
        if (character in last):
            if (character.islower()):
                sum = sum + ord(character) - 96
            else:
                sum = sum + ord(character) - 38
            break

print(sum)
