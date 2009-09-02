#!/usr/bin/env python

symbols = ("&", ".", ",", ":", ";", "?", "!", "-", "(", ")")

cnt = 0
for line in file("prob3_in.txt"):
    for symbol in symbols:
        line = line.replace(symbol, "")
    cnt += len(line.split())
print "This file contains %s words." % cnt
