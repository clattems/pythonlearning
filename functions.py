#!/usr/local/bin/python3
def loops():
    shoppingList = ["milk", "eggs", "cheese"]
    for i in shoppingList:
        day = "Wed"
        if day == "Tuesday":
            print(i)
        else:
            print("Hello, today is not the day")
print(loops())

def multiply(num1, num2):
    total = num1 * num2
    return total
print(multiply(10,23))
