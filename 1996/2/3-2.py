#!/usr/bin/env python

daysInMonth = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

def jan1(mm, dd, yyyy):
    return ((36 + (yyyy - 1) + ((yyyy - 1) / 4) - ((yyyy - 1) / 100) + ((yyyy - 1) / 400)) % 7)

def leap(yyyy):
    return ((((yyyy % 4) == 0) and ((yyyy % 100) != 0)) or ((yyyy % 400) == 0))

def validDay(mm, dd, yyyy):
    return (daysInMonth[mm - 1] + (leap(yyyy) and mm == 2))

def valid(mm, dd, yyyy):
    return ((mm > 0) and (mm <= 12) and (dd > 0) and (dd <= validDay(mm, dd, yyyy)) and (yyyy > 0))

fin = file("prob2_in.txt", "r")
while 1:
    dp, dd, mm, yyyy = 0, 0, 0, 0
    line = fin.readline()
    if line == "":
        break
    if line[-1] == "\n":
        line = line[:-1]
    (mm, dd, yyyy) = line.split("/")
    mm = int(mm)
    dd = int(dd)
    yyyy = int(yyyy)
    if not valid(mm, dd, yyyy):
        print "Invalid date in the input."
        continue
    dp = sum(daysInMonth[0:mm-1]) + dd + jan1(mm, dd, yyyy) - 1
    print "%s/%s/%s falls on a %s" % (mm, dd, yyyy, days[dp % 7])
