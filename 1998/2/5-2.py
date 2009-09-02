#!/usr/bin/env python

import sys

def clear(grid, dim, x, y):
    grid[x][y] = 0
    for i in xrange(-1,2):
        for j in xrange(-1,2):
            if x+i in dim and y+j in dim and grid[x+i][y+j]:
                clear(grid, dim, x + i, y + j)

targets = 0
dim = xrange(int(sys.stdin.readline()))
grid = map(lambda x: map(int, x), map(list, sys.stdin.read().splitlines()))
for i in dim:
    for j in dim:
        if grid[i][j]:
            targets += 1
            clear(grid, dim, i, j)
print "There are %s targets in the current image." % targets
