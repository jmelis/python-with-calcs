from random import randint

magic_number = randint(1, 100)

while True:
    guess = int(input("Guess the magic number: "))

    if guess < magic_number:
        print("Too low")

    if guess > magic_number:
        print("Too high")

    if guess == magic_number:
        print("You got it!")
        break
