#!/usr/bin/env python

import sys, datetime, calendar

for line in sys.stdin:
    m, d, y = map(int, line.split('/'))
    try:
        print "%s/%s/%s falls on a %s" % (m, d, y, calendar.day_name[datetime.date(y, m, d).weekday()])
    except ValueError:
        print "Invalid date in the input."
