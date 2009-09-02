#!/usr/bin/env python

for line in file("prob5_in.txt"):
    mono = True
    up = line[0] < line[1]
    for i in xrange(len(line) - 1):
        if up and line[i] >= line[i + 1] or not up and line[i] <= line[i + 1]:
            mono = False
    if mono:
        print line
