#!/opt/rh/python33/root/usr/bin/python3

"""
This function measures the amount of time it takes for your
program to run by creating two time variables, time1 and time2.
Time1 is the time that it is when the program starts, and time2 is
the time after it's finished. this function is called numbers
"""
import time
def numbers(max):
    time1 = time.time()
    for i in range(0,max):
        print(i)
    time2 = time.time()
    print(str(time2-time1))

print(numbers(4))

"""
using a tupple, call asctime to print out the time how you want it
format in the tup is Y, M, D, H, M, S, DOW, DOY, DST.
"""
tup = (2016, 9, 9, 12, 0, 15, 6, 0, 0)

print(time.asctime(tup))

"""
Messing with the display of time. This would be for a program
you're writing or something. The values are pulled from the
positions in the output of time.timelocal()
time.struct_time(tm_year=2016, tm_mon=9, tm_mday=4, tm_hour=18, tm_min=21, tm_sec=35, tm_wday=6, tm_yday=248, tm_isdst=1
"""
t = time.localtime()
year = t[0]
day = t[2]
month = t[1]
print(year)
print(day)
print(str(day) + "/" + str(month) + "/" + str(year))

"""
time.sleep function can slow down output

"""

for i in range(0,5):
    print(i)
    time.sleep(1)
