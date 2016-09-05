#!/usr/local/bin/python3
#Strings
sen = "Hello %s, you're invited to my birthday"
bone = ["steve", "bill", "amy"]
for i in bone:
    print(sen%(i))

"""
print certain parts of a string (forth on in this example)
"""
print(sen[3:])
print(sen[0:4])
