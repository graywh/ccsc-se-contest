#!/usr/bin/env python

import sys

keys = {
        'a': '2', 'b': '22', 'c': '222',
        'd': '3', 'e': '33', 'f': '333',
        'g': '4', 'h': '44', 'i': '444',
        'j': '5', 'k': '55', 'l': '555',
        'm': '6', 'n': '66', 'o': '666',
        'p': '7', 'q': '77': '777', 's': '7777',
        't': '8', 'u': '88', 'v': '888',
        'w': '9', 'x': '99', 'y': '999', 'z': '9999',
        ' ': '*',
        }

def pause(p, n):
    if keys[p][0] == keys[n][0] and keys[p] != "*":
        return "(PAUSE)"
    else:
        return ""

for l in sys.stdin:
    l = l.strip().lower()
    if l == "*":
        break
    sys.stdout.write(keys[l[0]])
    for i in xrange(1, len(l)):
        sys.stdout.write(pause(l[i-1], l[i]))
        sys.stdout.write(keys[l[i]])
    sys.stdout.write("\n")
