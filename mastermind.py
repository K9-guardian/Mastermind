import json
import random

words = json.load(open("words.json"))
choice = random.choice(words)
guess = "++++"

while True:
    guess = input("Enter a four letter word: ")

    if guess == choice:
        print("Congrats")
        break

    count = 0

    if len(guess) != 4:
        print("String length must be four" + "\n")
    else:
        for i in range(4):
            if guess[i] == choice[i]:
                count += 1
        print(str(count) + "\n")