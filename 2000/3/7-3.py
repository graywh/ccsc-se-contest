#!/usr/bin/env python

import sys

ln = 1
for line in sys.stdin:
    if line == "":
        break
    if line[-1] == "\n":
        line = line[:-1]
    nofreqs = 1
    cnt = 0
    freq = [0] * 26
    for ch in line:
        ch = ch.lower()
        i = ord(ch)
        if ch <= "z" and ch >= "a":
            freq[i - ord("a")] += 1
        cnt += 1
    print "Line %s: " % ln,
    for i in xrange(26):
        if 20 * freq[i] > 3 * cnt:
            print chr(i + ord("A")), "is a super freq.",
            nofreqs = 0
    if nofreqs:
        print "There are no super freqs.",
    print
    ln += 1
