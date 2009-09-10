#!/usr/bin/env python

import sys

for line in sys.stdin.readlines():
    count = 0
    x = 1
    for l in line:
        if x >= 0:
            count += 1
            if l == 'e':
                x += 1
            else:
                x -= 1
    if x >= 0:
        print -1
    else:
        print count
