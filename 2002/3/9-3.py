#!/usr/bin/env python

import sys

for line in sys.stdin:
    groups = set()
    count = 0
    for l in line:
        if l == 'A':
            count += 1
        else:
            if count > 0:
                groups.add(count)
            count = 0
    if count > 0:
        groups.add(count)
    print len(groups)
