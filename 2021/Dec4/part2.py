import os
import pathlib
import numpy as np

def play(card, num) -> bool:
    for y in range(5):
        for x in range(5):
            if card[y][x] == num:
                card[y][x] = -1
    return checkBingo(card)

def checkBingo(card) -> bool:
    bingo = False
    for y in range(5):
        colSum = 0
        rowSum = 0
        for x in range(5):       
            rowSum += card[y][x]
            colSum += card[x][y]
        if rowSum == -5 or colSum == -5:
            bingo = True
    return bingo            

def solutionSum(card) -> int:
    sum = 0
    for y in range(5):
        for x in range(5):
            if card[y][x] != -1:
                sum += card[y][x]
    return sum

dir = pathlib.Path(__file__).parent.absolute()

inputData = open(os.path.join(dir, "input.txt"))
data = inputData.split("\n\n")
calledNumbers = [int(x) for x in data[0].split(",")]
rawCards = data[1::]
bingoCards = []
for card in rawCards:
    newCard = card.splitlines()
    finalCard = []
    for y in range(5):
        line = [int(x) for x in newCard[y].split()]
        finalCard.append(line)
    bingoCards.append(finalCard)

solution = -1
for num in calledNumbers:
    for card in bingoCards:
        if not checkBingo(card):
            result = play(card, num)
            if result:
                solution = solutionSum(card)*num

print(f"Answer: {solution}")
