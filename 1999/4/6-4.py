#!/usr/bin/env python

import sys

while True:
    line = sys.stdin.readline()
    if line == "":
        break
    dim = int(line.split()[0])
    diag = 0
    magic = 1
    grid = []
    for i in xrange(dim):
        g = map(int, sys.stdin.readline().split())
        g.append(0)
        grid.append(g)
    grid.append([0] * (dim + 1))
    for i in xrange(dim):
        grid[dim][dim] += grid[i][i]
        diag += grid[dim - i - 1][i]
        for j in xrange(dim):
            grid[i][dim] += grid[i][j]
            grid[dim][j] += grid[i][j]
    for i in xrange(dim):
        if grid[i][dim] != diag:
            magic = 0
        if grid[dim][i] != diag:
            magic = 0
    if grid[dim][dim] != diag:
        magic = 0
    if magic:
        print "HOCUS"
    else:
        print "POCUS"
