#!/usr/bin/env python

import sys

class PTree:
    class Node:
        def __init__(self, d):
            self.data = d
            self.left = None
            self.right = None

    def __init__(self, line):
        self.isPalin = 0
        self.pal = ''
        self.root = self.create(line)
        s = ''
        self.traverseAll(self.root, s)

    def isPal(self):
        return self.isPalin

    def getPal(self):
        return self.pal

    def create(self, line):
        line.pop(0)
        ch = line.pop(0)
        if ch == ')':
            return None
        tmp = PTree.Node(ch)
        tmp.left = self.create(line)
        tmp.right = self.create(line)
        line.pop(0)
        return tmp

    def traverseAll(self, n, s):
        s = s + str(n.data)
        if n.left == None and n.right == None:
            self.isPalin = self.isPalindrome(s)
        if self.isPalin:
            self.pal = s
        if n.left != None and not self.isPalin:
            self.traverseAll(n.left, s)
        if n.right != None and not self.isPalin:
            self.traverseAll(n.right, s)

    def isPalindrome(self, s):
        for i in xrange(len(s) - 1):
            if s[i] != s[-i - 1]:
                return 0
        return 1

cnt = 1
for line in sys.stdin:
    line = list(line)
    t = PTree(line)
    print "Tree %s is" % cnt,
    if t.isPal():
        print "a palintree. Its palintree is %s." % t.getPal()
    else:
        print "not a palintree."
    cnt += 1
