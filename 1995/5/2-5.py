#!/usr/bin/env python

def getOne(n):
    return n % 10

def getTen(n):
    return (n % 100) / 10

def getHund(n):
    return n / 100

import sys

fin = file("prob5_in.txt", "r")
cnt = 1
while 1:
    act = fin.readline()
    if act == "":
        break
    line = fin.readline()
    if act[-1] == "\n":
        act = act[:-1]
    if line[-1] == "\n":
        line = line[:-1]
    if act == "encode":
        code = []
        print "Message",cnt,"(encoded): ",
        for i in xrange(len(line)):
            ch = ord(line[i])
            if ch > 99:
                code.append(getHund(ch))
            code.append(getTen(ch))
            code.append(getOne(ch))
        while code != []:
            sys.stdout.write(str(code.pop()))
        print
    elif act == "decode":
        msg = []
        print "Message",cnt,"(decoded): ",
        i = 0
        while i < len(line):
            ch1 = line[i]
            ch2 = line[i + 1]
            i += 2
            n = 10 * int(ch2) + int(ch1)
            if n < 23:
                n += 100
                i += 1
            msg.append(chr(n))
        while msg != []:
            sys.stdout.write(msg.pop())
        print
    cnt += 1
