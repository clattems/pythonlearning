#!/usr/local/bin/python3
students = {"eric":14, "bob":15}
print(len(students))
print(students.values())
students2 = {"john":14, "mike":15}
students.update(students2)
print(students)
