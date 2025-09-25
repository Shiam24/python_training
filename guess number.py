import random

secret_number = random.randint(1, 20)
print("Welcome To The Game")
guess = int(input("Enter your Guess value: "))

for i in range(1, 4):

    if guess == secret_number:
        print("YOU WIN")
        break
    elif guess < secret_number:
        print("Your guess is lower than my secret_number")
    elif guess > secret_number:
        print("Your guess is higher than my secret_number")
    else:
        print("Your guess is not in random numbers")

           
