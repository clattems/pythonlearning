#!/opt/rh/python33/root/usr/bin/python3
class Parent:
    counter = 10
    """docstring for ."""
    def __init__(self):
        print("ClassInit")
    def parentFunc(self):
        print("Parent being called")
    def setCounter(self, num):
        Parent.counter = num
    def showCounter(self):
        print(str(Parent.counter))

class Child(Parent):
    """docstring for ."""
    def __init__(self):
        print("Child class init")
    def childFunc(self):
        print("childFunc being called")

c = Child()



c.setCounter(20)
c.showCounter()
