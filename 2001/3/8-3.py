#!/usr/bin/env python

import sys

channel = 1
for line in sys.stdin:
    if line == "":
        break
    line = line.split()
    ary = []
    for i in line:
        ary.append(int(i))
    cross = 0
    for i in xrange(1, len(ary)):
        for j in xrange(i):
            if ary[i] < ary[j]:
                cross += 1
    print "There are %s wire crossings in routing channel %s." % (cross, channel)
    channel += 1
