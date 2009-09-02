#!/usr/bin/env python

import datetime, calendar

for line in file('prob2_in.txt', 'r'):
    m, d, y = map(int, line.split('/'))
    try:
        print "%s/%s/%s falls on a %s" % (m, d, y, calendar.day_name[datetime.date(y, m, d).weekday()])
    except ValueError:
        print "Invalid date in the input."
