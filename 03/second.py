file = open("input.txt", "r")
rawLines = file.readlines()

lines = []
for i in rawLines:
    lines.append(i.rstrip("\n"))

sum = 0

i = 0
while i < len(lines):
    rucksacks = lines[i: i + 3]
    for character in rucksacks[0]:
        if (character in rucksacks[1] and character in rucksacks[2]):
            if (character.islower()):
                sum = sum + ord(character) - 96
            else:
                sum = sum + ord(character) - 38
            break

    i = i + 3

print(sum)
