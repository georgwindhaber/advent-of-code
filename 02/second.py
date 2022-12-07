file = open("input.txt", "r")
lines = file.readlines()

currentSum = 0

plays = {"A": {"beats": "B", "looses": "C"},
         "B": {"beats": "C", "looses": "A"},
         "C": {"beats": "A", "looses": "B"}}

playValues = {"A": 1, "B": 2, "C": 3}

for line in lines:
    rawLine = line.replace("\n", "")
    values = rawLine.split(" ")
    enemy = values[0]
    myself = values[1]

    # Loose
    if (myself == "X"):
        currentSum = currentSum + 0 + playValues[plays[enemy]["looses"]]
    # Draw
    elif (myself == "Y"):
        currentSum = currentSum + 3 + playValues[enemy]
    # Win
    else:
        currentSum = currentSum + 6 + playValues[plays[enemy]["beats"]]

print(currentSum)
