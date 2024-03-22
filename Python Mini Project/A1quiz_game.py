print("Welcome to the quiz")

playing: str = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay let's play the game :))")

answer = input("What does CPU stands for? ").lower()

if answer == "central processing unit":
    print("Correct")
else:
    print("Incorrect")

answer = input("What does GPU stands for? ").lower()

if answer == "graphics processing unit":
    print("Correct")
else:
    print("Incorrect")

answer = input("What does RAM stands for? ").lower()

if answer == "random access memory":
    print("Correct")
else:
    print("Incorrect")

answer = input("What does PSU stands for? ").lower()

if answer == "power supply unit":
    print("Correct")
else:
    print("Incorrect")

answer = input("What does HDD stands for? ").lower()

if answer == "hard disk drive":
    print("Correct")
else:
    print("Incorrect")
