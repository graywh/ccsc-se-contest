#!/usr/bin/env python

import sys

for line in sys.stdin.readlines():
    a,b,c,n = map(int, line.split(','))
    total = a + b + c
    for i in xrange(3,n):
        d = a + b + c
        total += d
        a, b, c = b, c, d
    print "The answer is: %s" % total
