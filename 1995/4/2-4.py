#!/usr/bin/python
import sys

chk = [1,0,0,0,0,0,1]
for line in file('prob4.in', 'r'):
    q = map(int, list(line))
    recording = False
    for i in xrange(len(q) / 7):
        if q[i*7:(i+1)*7] == chk:
            recording = not recording
        elif recording:
            sys.stdout.write(chr(sum([x * 2 ** (6-i) for i,x in enumerate(q[i*7:(i+1)*7])])))
    sys.stdout.write('\n')
