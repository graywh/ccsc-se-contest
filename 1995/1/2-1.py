#!/usr/bin/env python

import sys

for line in sys.stdin:
    a,b = map(int, line.split())
    print "%s X %s =" % (a,b),
    sum = 0
    while a > 0:
        if a % 2:
            print b,
            sum += b
            if a > 1:
                print "+",
        a /= 2
        b *= 2
    print "= %s" % sum
