#!/opt/rh/python33/root/usr/bin/python3
class Students():
    pass
    """docstring for ."""
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
#here is an example of a funtion in a class
    def displayStuden(self):
            return("Student namne is " + self.name + " and age is " + str(self.age))

student1 = Students("Bob", 12, "7th")

print(student1.name)

print(student1.displayStuden())

#check to see if attribute is present
print(hasattr(student1, "age"))

#add attribute to class
setattr(student1, 'lunch', "yes")

print(hasattr(student1, "lunch"))

print(getattr(student1, "age"))
