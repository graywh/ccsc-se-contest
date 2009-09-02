#!/usr/bin/env python

import sys

for line in sys.stdin:
    if line == "":
        break
    line = line.split()
    n = int(line[0])
    cnt = 0
    tmp = n
    while tmp != 4 and tmp != 2 and tmp != 1:
        cnt += 1
        if not tmp % 2:
            tmp /= 2
        else:
            tmp = (tmp * 3) + 1
    print "%s steps were necessary for %s." % (cnt, n)
