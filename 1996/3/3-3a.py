#!/usr/bin/env python

import sys

symbols = ("&", ".", ",", ":", ";", "?", "!", "-", "(", ")")

cnt = 0
for line in sys.stdin:
    for symbol in symbols:
        line = line.replace(symbol, "")
    cnt += len(line.split())
print "This file contains %s words." % cnt
