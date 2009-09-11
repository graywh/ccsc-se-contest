#!/usr/bin/env python

import sys

for line in sys.stdin:
    numcoins = int(line)
    p1 = []
    p2 = []
    worst = numcoins * (numcoins + 1) / 4
    best = numcoins * (numcoins + 1) / 2 - worst
    sum1 = 0
    sum2 = 0
    for i in xrange(numcoins,0,-1):
        if sum1 + i <= best:
            sum1 += i
            p1.append(i)
        else:
            sum2 += i
            p2.append(i)
    p1.reverse()
    p2.reverse()
    print
    print "Number of coins:", numcoins
    print "Pile 1 contains",
    print ", ".join(map(str, p1)),
    print "with value %s." % sum1
    print "Pile 2 contains",
    print ", ".join(map(str, p2)),
    print "with value %s." % sum2
