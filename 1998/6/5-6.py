#!/usr/bin/env python

import sys

mos = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for line in sys.stdin:
    line = line.strip()
    if line == "":
        break
    ln = line.split()
    tmp = int(ln[0])
    month = 0
    mos[1] = 28
    year = 1900 + tmp / 1000
    if year == 1900:
        year += 100
    if year % 4 == 0:
        mos[1] += 1
    day = tmp % 1000
    while day > mos[month]:
        day -= mos[month]
        month += 1
    month += 1
    if month < 10:
        month = "0" + str(month)
    if day < 10:
        day = "0" + str(day)
    print "%s/%s/%s" % (month, day, year)
