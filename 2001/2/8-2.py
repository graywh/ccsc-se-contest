#!/usr/bin/env python

class Point:
    def __init__(self, r = 0, c = 0, p = None):
        self.row = r
        self.col = c
        if p is not None:
            self.row = p.row
            self.col = p.col

    def __cmp__(self, p):
        if self.row == p.row and self.col == p.col:
            return 0
        if self.row < p.row or self.col < p.col:
            return -1
        else:
            return 1

    def __add__(self, p):
        return Point(self.row + p.row, self.col + p.col)
        
    def __str__(self):
        return "(%s, %s)" % (self.row, self.col)

def isValid(p, dim):
    return p.row > 0 and p.row <= dim and p.col > 0 and p.col <= dim

fin = file("prob2.in")
UP = Point(-1, 0)
DOWN = Point(1, 0)
LEFT = Point(0, -1)
RIGHT = Point(0, 1)
while 1:
    line = fin.readline()
    if line == "":
        break
    line = line.split()
    gridDim = int(line[0])
    line = fin.readline().split()
    start = Point(int(line[0]), int(line[1]))
    line = fin.readline().split()
    end = Point(int(line[0]), int(line[1]))
    cnt = 0
    complete = 0
    visited = []
    visit = []
    grid = []
    for i in xrange(gridDim):
        line = fin.readline().split()
        ln = []
        for i in xrange(gridDim):
            ln.append(int(line[i]))
        grid.append(ln)
    visit.append(start)
    #print "\n".join([" ".join([str(i) for i in ln]) for ln in grid])
    while not complete:
        num = len(visit)
        cnt += 1
        for i in xrange(num):
            here = visit.pop(0)
            visited.append(here)
            if here == end:
                complete = 1
                break
            hereU = here + UP
            hereD = here + DOWN
            hereL = here + LEFT
            hereR = here + RIGHT
            if isValid(hereU, gridDim) and not visited.count(hereU):
                if grid[hereU.row - 1][hereU.col - 1] == 0:
                    visit.append(hereU)
            if isValid(hereD, gridDim) and not visited.count(hereD):
                if grid[hereD.row - 1][hereD.col - 1] == 0:
                    visit.append(hereD)
            if isValid(hereL, gridDim) and not visited.count(hereL):
                if grid[hereL.row - 1][hereL.col - 1] == 0:
                    visit.append(hereL)
            if isValid(hereR, gridDim) and not visited.count(hereR):
                if grid[hereR.row - 1][hereR.col - 1] == 0:
                    visit.append(hereR)
        if len(visit) == 0:
            break
    if complete:
        print "There are %s squares on a shortest path" % cnt,
    else:
        print "No paths were found",
    print "from %s to %s" % (start, end)
