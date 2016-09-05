import random

compnum = random.randint(0,10)
while True:
    usernum = int(input("enter your guess between one and ten: "))
    if usernum > compnum:
        print("Guess Lower")
    elif usernum < compnum:
        print("Guess Higher")
    elif usernum > 10:
        print("not a valid number")
    else:
        print("Congrats, you just won the game!")
        break
