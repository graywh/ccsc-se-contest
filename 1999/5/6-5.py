#!/usr/bin/env python

import sys

train = 1
for line in sys.stdin.read().splitlines():
    ln = map(int, line.split())
    cnt = ln[0]
    num = ln[1]
    incoming = ln[2:]
    holds = []
    for i in xrange(num):
        holds.append([])
    out = 0
    while len(incoming) > 0:
        cur = incoming.pop()
        if cur - 1 == out:
            out = cur
            move = 1
            while move:
                move = 0
                for h in holds:
                    if len(h) != 0:
                        if h[-1] - 1 == out:
                            move = 1
                            out = h.pop()
        else:
            i = 0
            while i < len(holds):
                tmp = holds[i]
                if len(tmp) == 0:
                    tmp.append(cur)
                    holds[i] = tmp
                    break
                elif cur < tmp[-1]:
                    tmp.append(cur)
                    holds[i] = tmp
                    break
                i += 1
            if i == len(holds):
                holds.append([cur])
    if len(holds) == num:
        print "Train", train, "can be rearranged."
    else:
        print "Train", train, "cannot be rearranged. At least",
        print len(holds), "holding tracks would be needed."
    train += 1
