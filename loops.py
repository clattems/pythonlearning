#!/usr/local/bin/python3
#for loops
for i in range(0,5):
    print(i)

shoppingList = ["milk", "eggs", "cheese"]
for i in shoppingList:
    day = "Wed"
    if day == "Tuesday":
        print(i)
    else:
        print("Hello, today is not the day")
#  count by 3s between 0 and 100 and print out
for i in range(0, 101, 20):
    print(i)

#nested for loops
#for i in range(2,30):
#    counter = 0
#    while j < i:
#        if i % j == 0:
#            counter = 1
#        else:
#            j = j + 1
#
#            if counter == 0:
#                print(str(i) + "is a prime number")
#                counter = 0
#            else:
#                counter = 0
