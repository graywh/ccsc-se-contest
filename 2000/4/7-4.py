#!/usr/bin/env python

import sys

cnt = 1
for line in sys.stdin:
    if line == "":
        break
    if line[-1] == "\n":
        lin = line[:-1]
    sentence = line.split()
    for i in xrange(len(sentence)):
        word = sentence.pop(0).lower()
        if word[-1] > "z" or word[-1] < "a":
            word = word[:-1]
        if word != "":
            sentence.append(word)
    sorted = sentence[:]
    sorted.sort()
    reversed = sorted[:]
    reversed.reverse()
    print "Sentence", cnt, "is",
    if sorted != sentence and reversed != sentence:
        print "non-monotonic."
    else:
        print "monotonic."
    cnt += 1
