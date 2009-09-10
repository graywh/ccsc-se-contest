#!/usr/bin/env python

import sys

for line in sys.stdin.readlines():
    x = int(line)
    y = x / 60
    z = x % 60
    total = y / 2 * 300
    if y % 2 == 0:
        total += z * 15
    else:
        total += 900
        total -= z * 10
    if x <= 720 and x >= 0:
        print total
