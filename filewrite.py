#!/opt/rh/python33/root/usr/bin/python3
file1 = open("/learn/pythonlearning/python.txt", "w")

file1.write("entering text \n lets see if this works")

file1 = open("/learn/pythonlearning/python.txt", "r")

file1.read()

file1 = open("/learn/pythonlearning/python.txt", "a")

file1.write("\n this is some text")
