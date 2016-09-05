#!/opt/rh/python33/root/usr/bin/python3
file1 = open("/learn/pythonlearning/python.txt", "r")
"""
Print the file contents, list how many characters there are
reset the curser to the beginning
last is print the first 21 characters
"""
print(file1.read())
print(file1.tell())
file1.seek(0,0)
print(file1.tell())
print(file1.read(21))
