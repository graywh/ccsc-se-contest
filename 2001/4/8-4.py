#!/usr/bin/env python

import sys

points = {0:500, 1:300, 2:250, 3:200, 4:150, 5:100, 6:75, 7:50, 8:25, 9:10, 10:0}

while True:
    line = sys.stdin.readline()
    if line == "":
        break
    name = line.split()[0]
    print
    print "Score Summary for", name
    print "-----------------------"
    score = 0
    for i in xrange(1, 6):
        line = sys.stdin.readline()
        line = line.split()
        x = float(line[0])
        y = float(line[1])
        dist = (x * x + y * y) ** 0.5
        d = int(dist / 50)
        if (dist % 50) == 0 and d > 0:
            d -= 1
        if d > 10:
            d = 10
        n = points[d]
        score += n
        print "   Hit %s =%13d" % (i, n)
    print "              ---------"
    print "   Score =%13d" % score
