#!/usr/bin/env python

import sys

insig = []
for line in sys.stdin:
    amt, unit, dv, name = line.strip().split(' ', 3)
    if amt == "-1.0":
        break
    pct = int(float(amt) / float(dv) * 100)
    if pct == 0:
        insig.append(name)
    else:
        print '%s %s %s %s%%' % (name, amt, unit, pct)
print 'Provides no significant amount of:\n%s' % ('\n'.join(insig))
