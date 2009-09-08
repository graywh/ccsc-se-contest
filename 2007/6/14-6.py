#!/usr/bin/env python

import sys

def x(p):
    return p[0]

def y(p):
    return p[1]

def area(p1, p2, p3):
    return 0.5 * (
              (x(p1) * y(p2))
            + (x(p2) * y(p3))
            + (x(p3) * y(p1))
            - (x(p1) * y(p3))
            - (x(p2) * y(p1))
            - (x(p3) * y(p2))
            )

sys.stdin.readline()

points = [tuple([int(a) for a in l.split(',')]) for l in sys.stdin]

hull = []
p0 = points[0]
for p in points:
    if y(p) < y(p0):
        p0 = p
start = p0
hull.append(p0)

pn = None
while True:
    for p1 in points:
        if p1 == p0:
            continue
        if all([area(p0, p1, p2) >= 0 for p2 in points]):
            pn = p1
    if pn == start:
        break
    hull.append(pn)
    p0 = pn

for p in hull:
    print "(%s,%s)" % p
