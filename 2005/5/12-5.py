#!/usr/bin/env python

import sys

sys.stdin.readline()
for i in sys.stdin.read().splitlines():
    problem = map(int, i.split())
    print 1 - problem[0] + sum(problem[1:])
