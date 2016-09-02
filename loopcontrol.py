#!/opt/rh/python33/root/usr/bin/python3
counter = 0
while counter < 100:
    if counter == 4:
        break
    print(counter)
    counter = counter + 1


while counter < 100:
    if counter == 4:
        break
    else:
        pass
    print(counter)
    counter = counter + 1

for i in "Python":
    if i == "h":
        continue
    print(i)

for i in range(0,5):
    if i < 2:
        continue
    print(i)
