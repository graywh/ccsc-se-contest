#!/usr/bin/env python

days = [31,28,31,30,31,30,31,31,30,31,30,31]
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

fin = file("prob2_in.txt", "r")
while 1:
    line = fin.readline()
    if line == "":
        break
    if line == "From veep@whitehouse.gov\n":
        line = fin.readline()
        if line == "To buddha@whitehouse.gov\n":
            days[1] = 28
            dd = 0
            line = fin.readline()
            ln = line.split()
            day = ln[1]
            month = ln[2]
            dd = int(ln[3][:-1])
            yyyy = int(ln[4])
            if yyyy % 4 == 0 and yyyy % 100 or yyyy % 400 == 0:
                days[1] += 1
            for i in xrange(12):
                if month == months[i]:
                    mm = i
            newmm = mm
            newdd = dd + 28
            newyyyy = yyyy
            if newdd > days[mm]:
                newdd -= days[mm]
                newmm += 1
            if newmm == 12:
                newmm = 0
                newyyyy += 1
            print "From buddha@whitehouse.gov"
            print "To veep@whitehouse.gov"
            print "Date %s %s %s, %s" % (day, month, dd, yyyy)
            print "Subject Re: BM"
            print
            print "Thank you for advising me of your BM. You may not have"
            print "another BM until %s %s %s, %s." % (day, months[newmm], newdd, newyyyy)
