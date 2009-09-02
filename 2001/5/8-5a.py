#!/usr/bin/env python

import sys

def parse(line):
    ch = line[0]
    line = line[1:]
    d = ord(ch)
    if d >= ord('0') and d <= ord('9'):
        sys.stdout.write(ch)
    else:
        sys.stdout.write("(")
        line = parse(line)
        sys.stdout.write(' ')
        sys.stdout.write(ch)
        sys.stdout.write(' ')
        line = parse(line)
        sys.stdout.write(")")
    return line

for line in sys.stdin:
    if line == "":
        break
    line = parse(line)
    print
