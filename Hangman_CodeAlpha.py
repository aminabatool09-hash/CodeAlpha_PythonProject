import random

words = ["apple", "banana", "grape"]
word = random.choice(words)

guessed = ""
chances = 6

print("Hangman Game")

while chances > 0:
    display = ""

    for i in word:
        if i in guessed:
            display += i
        else:
            display += "_"

    print(display)

    if display == word:
        print("You Win!")
        break

    letter = input("Enter letter: ")

    guessed = guessed + letter

    if letter not in word:
        chances = chances - 1
        print("Wrong! Chances left:", chances)

if chances == 0:
    print("You Lose! Word was:", word)