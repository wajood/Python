import random

secret_number = random.randint(1, 100)
attempts = 5

for i in range(attempts):
    guess = int(input("Guess the number (1-100): "))

    if guess == secret_number:
        print("You won!")
        break
    else:
        print("Wrong guess")

else:
    print("Game Over! Number was:", secret_number)