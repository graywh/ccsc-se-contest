#!/usr/bin/env python

import sys

cnt = 1
for line in sys.stdin:
    if line == "":
        break
    line = line.split()
    bagC = int(line[0])
    cont = int(line[1])
    test = []
    test2 = []
    perc = []
    for i in xrange(cont * 2):
        test.append(int(line[i + 2]))
    for j in xrange(cont):
        test2.append(test[j + cont] / float(test[j]))
        perc.append(0)
    tmp = 0
    while tmp < bagC:
        maxi = 0
        val = 0
        for k in xrange(cont):
            if test2[k] > maxi:
                maxi = test2[k]
                val = k
        if maxi != 0:
            if tmp + test[val] <= bagC:
                tmp += test[val]
                perc[val] = 100
            else:
                perc[val] = (bagC - tmp) * 100 / test[val]
                tmp = bagC
            test2[val] = 0
        else:
            break
    print "Game", cnt
    print "------"
    for q in xrange(cont):
        print "Container %s: %s" % (q + 1, perc[q])
    cnt += 1
