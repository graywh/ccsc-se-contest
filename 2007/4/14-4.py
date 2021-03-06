#!/usr/bin/env python

import sys

def needed(x, p):
    x.sort()
    s = sum(x)
    mx = x[2]
    mn = x[0]
    md = x[1]
    if s - mx > p:
        return None
    elif mx + mn > p:
        return 2 * (mx + mn)
    elif 2 * (mx + mn) > p:
        return 2 * (md + mn)
    else:
        return mn + md

paper = int(sys.stdin.readline().split()[2])
sys.stdin.readline()

for i,l in enumerate(sys.stdin.read().splitlines()):
    print "Gift %s" % (i+1),
    d = [int(x) for x in l.split('x')]
    n = needed(d, paper)
    if n is None:
        print "cannot be wrapped."
    else:
        print "needs %s inches." % n
