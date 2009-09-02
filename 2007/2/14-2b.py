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

def convert(l):
    for c in l:
        yield c
    yield ' '

def reduct(a, b):
    sys.stdout.write(keys[a])
    sys.stdout.write(pause(a,b))
    return b

for l in sys.stdin:
    l = l.strip().lower()
    if l == "*":
        break
    reduce(reduct, convert(l[1:]), l[0])
    sys.stdout.write("\n")
