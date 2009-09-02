#!/usr/bin/env python

import sys

print "Z  I  M  L  Length"
print "------------------"
for line in sys.stdin.read().splitlines():
    z, i, m, l = map(int, line.split())
    cnt = 0
    print "%s %s %s %s" % (str(z).ljust(2), str(i).ljust(2), str(m).rjust(2), str(l).ljust(2)),
    start = ((z * l + i) % m)
    l = ((z * l + i) % m)
    if m == 1:
        print "ERROR"
        continue
    else:
        while 1:
            l = ((z * l + i ) % m)
            cnt += 1
            if start == l:
                break
        print str(cnt).rjust(3)
