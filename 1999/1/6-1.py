#!/usr/bin/env python

import sys

def moveRight(grid, r, c, dimR, dimC, pathFound):
    grid[r][c] = 'A'
    if ((r == dimR - 1) and (c == dimC - 1)):
        pathFound = 1
        dumpGrid(grid, dimR, dimC)
    if (isValid(grid, r + 1, c, dimR, dimC)):
        pathFound = pathFound or moveDown(grid, r + 1, c, dimR, dimC, pathFound)
    if (not pathFound and isValid(grid, r, c + 1, dimR, dimC)):
        pathFound = pathFound or moveRight(grid, r, c + 1, dimR, dimC, pathFound)
    if (not pathFound and isValid(grid, r - 1, c, dimR, dimC)):
        pathFound = pathFound or moveUp(grid, r - 1, c, dimR, dimC, pathFound)
    grid[r][c] = 'Y'
    return pathFound

def moveLeft(grid, r, c, dimR, dimC, pathFound):
    grid[r][c] = 'A'
    if ((r == dimR - 1) and (c == dimC - 1)):
        pathFound = 1
        dumpGrid(grid, dimR, dimC)
    if (isValid(grid, r - 1, c, dimR, dimC)):
        pathFound = pathFound or moveUp(grid, r - 1, c, dimR, dimC, pathFound)
    if (not pathFound and isValid(grid, r, c - 1, dimR, dimC)):
        pathFound = pathFound or moveLeft(grid, r, c - 1, dimR, dimC, pathFound)
    if (not pathFound and isValid(grid, r + 1, c, dimR, dimC)):
        pathFound = pathFound or moveDown(grid, r + 1, c, dimR, dimC, pathFound)
    grid[r][c] = 'Y'
    return pathFound

def moveDown(grid, r, c, dimR, dimC, pathFound):
    grid[r][c] = 'A'
    if ((r == dimR - 1) and (c == dimC - 1)):
        pathFound = 1
        dumpGrid(grid, dimR, dimC)
    if (isValid(grid, r, c - 1, dimR, dimC)):
        pathFound = pathFound or moveLeft(grid, r, c - 1, dimR, dimC, pathFound)
    if (not pathFound and isValid(grid, r + 1, c, dimR, dimC)):
        pathFound = pathFound or moveDown(grid, r + 1, c, dimR, dimC, pathFound)
    if (not pathFound and isValid(grid, r, c + 1, dimR, dimC)):
        pathFound = pathFound or moveRight(grid, r, c + 1, dimR, dimC, pathFound)
    grid[r][c] = 'Y'
    return pathFound

def moveUp(grid, r, c, dimR, dimC, pathFound):
    grid[r][c] = 'A'
    if ((r == dimR - 1) and (c == dimC - 1)):
        pathFound = 1
        dumpGrid(grid, dimR, dimC)
    if (isValid(grid, r, c + 1, dimR, dimC)):
        pathFound = pathFound or moveRight(grid, r, c + 1, dimR, dimC, pathFound)
    if (not pathFound and isValid(grid, r - 1, c, dimR, dimC)):
        pathFound = pathFound or moveUp(grid, r - 1, c, dimR, dimC, pathFound)
    if (not pathFound and isValid(grid, r, c - 1, dimR, dimC)):
        pathFound = pathFound or moveLeft(grid, r, c - 1, dimR, dimC, pathFound)
    grid[r][c] = 'Y'
    return pathFound

def isValid(grid, r, c, dimR, dimC):
    return (r > -1) and (r < dimR) and (c > -1) and (c < dimC) and (grid[r][c] == 'Y')

def dumpGrid(grid, dimR, dimC):
    for i in xrange(dimR):
        print "  ",
        for j in xrange(dimC):
            if grid[i][j] == 'X' or grid[i][j] == 'Y':
                print "-",
            else:
                print "0",
        print

cnt = 1
while 1:
    line = sys.stdin.readline()
    if line == "":
        break
    dimR, dimC = line.split()
    dimR = int(dimR)
    dimC = int(dimC)
    grid = [0] * dimR
    for i in xrange(dimR):
        line = sys.stdin.readline()
        ln = [0] * dimC
        for j in xrange(dimC):
            ln[j] = line[j]
        grid[i] = ln
    print
    print "Maze %s:" % cnt
    pathFound = moveRight(grid, 0, 0, dimR, dimC, 0)
    if not pathFound:
        print "   No path exists."
    cnt += 1
