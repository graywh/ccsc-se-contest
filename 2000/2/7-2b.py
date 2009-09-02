#!/usr/bin/env python

import sys, datetime, calendar

months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

while 1:
    line = sys.stdin.readline()
    if line == '':
        break
    if line == 'From veep@whitehouse.gov\n':
        line = sys.stdin.readline()
        if line == 'To buddha@whitehouse.gov\n':
            line = sys.stdin.readline().split()
            dow = line[1]
            day = datetime.date(int(line[4]), months.index(line[2])+1, int(line[3][:-1]))
            newday = day + datetime.timedelta(days=28)
            print "From buddha@whitehouse.gov"
            print "To veep@whitehouse.gov"
            print "Date %s %s %s, %s" % (dow, calendar.month_name[day.month], day.day, day.year)
            print "Subject Re: BM"
            print
            print "Thank you for advising me of your BM. You may not have"
            print "another BM until %s, %s %s, %s." % (calendar.day_name[newday.weekday()], calendar.month_name[newday.month], newday.day, newday.year)
