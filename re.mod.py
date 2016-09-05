#!/opt/rh/python33/root/usr/bin/python3
import re
string = "the night was cold and dark and no one was there"
re.search("night", string)
#This is how you store output to a var
m = re.search("night", string)
print(m)
#save the starting positions to vairables (4th place and 9th)
start = m.start()
end = start + 5

print(start)
print(end)

#print the range, which will print "night"
print(string[start:end])
