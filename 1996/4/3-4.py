#!/usr/bin/env python

fin = file("buffy.dat")
msg = 1
while 1:
    line = fin.readline()
    if line == "":
        break
    if line[-1] == "\n":
        line = line[:-1]
    rows,cols = map(int, line.split())
    ary = []
    for i in xrange(rows):
        ary.append(fin.readline().split())
    print "Message", msg, "=>",
    j = cols - 1
    for i in xrange(rows):
        print ary[i][j],
        j -= 1
        if j < 0:
            j = cols - 1
    print
    msg += 1
