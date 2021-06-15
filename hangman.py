import random

name = input("What is your name? ")

print("Good luck! " + name)

words = ['rainbow', 'computer', 'science', 'programming', 'python', 'mathematics',
         'player', 'condition', 'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")
guesses = ''

turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You Win")
        print("The word is: " + word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("guess a character: ")
    # every input character will be stored in guesses
    guesses += guess

    if guess not in word:
        turns -= 1

        if turns == 0:
            print("You Lose")
            print("The word is: " + word)

        else:
            print("Wrong")
            print("You have", turns, 'more guesses')
