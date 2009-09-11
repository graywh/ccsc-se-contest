#!/usr/bin/env python

import sys

cnt = 1
for line in sys.stdin:
    line = map(int, line.split())
    caproom = line[0]
    n = line[1]
    conts = line[2:]
    conts.sort()
    conts.reverse()
    ship = []
    while caproom >= conts[-1]:
        ship.append(conts[-1])
        caproom -= conts.pop()
    if caproom > 0:
        for i in conts:
            for j in ship:
                if caproom + j >= i and j <= i:
                    caproom += j
                    caproom -= i
                    j = i
    print
    print "Ship", cnt
    print "------"
    print "Number of containers loaded:", len(ship)
    print "Weight under capacity:", caproom
    cnt += 1
