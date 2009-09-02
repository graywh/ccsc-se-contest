#!/usr/bin/env python

import sys

class Point:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

def distance(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

cnt = 1
while True:
    line = sys.stdin.readline()
    if line == "":
        break
    ships = line.split()
    ships = int(ships[0])
    plot = []
    for i in xrange(ships):
        line = sys.stdin.readline()
        line = map(float, line.split())
        pt = Point()
        pt.x = line[0]
        pt.y = line[1]
        plot.append(pt)
    mini = distance(plot[0], plot[1])
    n1 = 0
    n2 = 1
    for i in xrange(ships - 1):
        for j in xrange(i + 1, ships):
            tmp = distance(plot[i], plot[j])
            if tmp < mini:
                mini = tmp
                n1 = i
                n2 = j
    print "Fleet %s: Ship %s and Ship %s are the closeest pair." % (cnt, n1 + 1, n2 + 1)
    cnt += 1
