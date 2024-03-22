import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_num = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please type a number next time.")
        continue  # go back to the beginning of the loop

    if guess == random_num:
        print("You got it right!")
        break
    elif random_num > guess:
        print("Your guess is too low")
    else:
        print("Your guess is too high")


print("You got it in", guesses, "guesses")
