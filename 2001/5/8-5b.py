#!/usr/bin/env python

import sys

mem = []
extra = 0
for line in sys.stdin:
    if line == "":
        break
    if line[-1] == "\n":
        line = line[:-1]
    cont = 0
    for i in xrange(len(line)):
        ch = line[i]
        if cont:
            cont -= 1
            continue
        if ord(ch) >= ord('0') and ord(ch) <= ord('9'):
            sys.stdout.write(ch)
            while len(mem) and ord(line[i + 1]) >= ord('0') and ord(line[i + 1]) <= ord('9'):
                sys.stdout.write(' ' + mem.pop(0) + ' ' + line[i + 1] + ")")
                i += 1
                cont += 1
            if len(mem) and i < len(line):
                sys.stdout.write(mem.pop(0))
                extra += 1
        else:
            sys.stdout.write("(")
            mem.append(ch)
    for i in xrange(extra):
        sys.stdout.write(")")
    print
