#!/usr/bin/env python

import sys

def same(a, b):
    if len(a) != len(b):
        return False
    for i in xrange(len(a)):
        c = b[i:] + b[:i]
        if a == c:
            return True
        c.reverse()
        if a == c:
            return True
    return False

def reorder(a):
    while a[0] != min(a):
        a = a[1:] + a[:1]
    if a[1] > a[-1]:
        a.reverse()
        a = [a[-1]] + a[:-1]
    return a

def find(conf, size, coll=set(), arr=[], count=0):
    if len(arr) == size and arr[0] != arr[-1]:
        #sarr = ''.join(reorder(arr))
        for sarr in coll:
        #if not sarr in coll:
            if same(list(sarr), arr):
                return (coll, count)
        coll.add(''.join(arr))
        print ''.join(arr)
        return (coll, count + 1)
    else:
        ks = conf.keys()
        ks.sort()
        for k in ks:
            if (len(arr) == 0 or k != arr[-1]) and conf[k] > 0:
                conf[k] -= 1
                coll, count = find(conf, size, coll, arr + [k], count)
                conf[k] += 1
    return (coll, count)

i = 1
while True:
    l, c = [int(x) for x in sys.stdin.readline().split()]
    if l == 0 and c == 0:
        break
    config = {}
    for j in xrange(l):
        k = sys.stdin.readline().split()
        config[k[0][0]] = int(k[1])
    coll, t = find(config, c)
    print "Total number of possible seating arrangements = %s" % t
