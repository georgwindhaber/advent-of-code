file = open("input.txt", "r")
lines = file.readlines()

currentSum = 0

plays = {"X": {"beats": "C", "looses": "B", "playValue": 1},
         "Y": {"beats": "A", "looses": "C", "playValue": 2},
         "Z": {"beats": "B", "looses": "A", "playValue": 3}}

for line in lines:
    rawLine = line.replace("\n", "")
    values = rawLine.split(" ")
    enemy = values[0]
    myself = values[1]

    if (enemy == plays[myself]["beats"]):
        currentSum = currentSum + 6 + plays[myself]["playValue"]
    elif (enemy == plays[myself]["looses"]):
        currentSum = currentSum + 0 + plays[myself]["playValue"]
    else:
        currentSum = currentSum + 3 + plays[myself]["playValue"]

print(currentSum)
