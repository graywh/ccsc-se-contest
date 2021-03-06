#!/usr/bin/env python

import sys

trash = [",", ".", "!", "?", "\n", ":", ";"]
swap = ["Th", "Kh", "Wh", "Tr", "Sh", "Fl", "th", "kh", "wh", "tr", "sh", "fl"]

for line in sys.stdin:
    if line == "":
        break
    words = line.split()
    for word in words:
        end = ""
        for trsh in trash:
            if word[-1] == trsh:
                word = word[:-1]
                end = trsh
                break
        word = word[:-2]
        done = 0
        for swp in swap:
            if word[-2:] == swp:
                word = swp + word[:-2]
                done = 1
                break
        if done == 0:
            if word[-1] == "y":
                word = word[:-1]
            else:
                word = word[-1] + word[:-1]
        print "%s%s" % (word, end),
