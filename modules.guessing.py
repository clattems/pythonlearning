import random
usernum = int(input("enter your guess between one and three: "))
if usernum > 3:
    print("Too High Jackass")
    
compnum = random.randint(0,3)
if usernum == compnum:
    print("you win")
else:
    print("sorry you lost")
