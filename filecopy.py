#!/opt/rh/python33/root/usr/bin/python3
#target file
targetfile = input("Enter your file name: ")
#opens file
file1 = open(targetfile, "r")
#opens file that we'll be copying to
file2 = open("copiedfile.txt", "w")
#reads file1, and copies contents to file2
file2.write(file1.read())
file1.close()
file2.close()
