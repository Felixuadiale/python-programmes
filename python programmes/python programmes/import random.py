import random
number = random.randint(1,10)
number_of_guesses=0
while  number_of_guesses<5:
    guess=int(input("Welome to number game.Enter your guess(1,10)"))
    number_of_guesses=number_of_guesses+1
    if guess < number:
        print("Your guess is too low")
    if guess > number:
        print("Your guess is too high")
    if guess == number:
        break
if guess == number:
        print("You guessed the number in ",number_of_guesses)
else:
        print("You did not guess the number",number )