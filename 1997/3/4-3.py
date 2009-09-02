#!/usr/bin/env python

class WoodChuck:
    def __init__(self, name, tooth):
        self.name = name
        self.tooth = tooth

    def __cmp__(self, wc):
        return cmp(self.tooth,wc.tooth)

def bld(x):
    for i in x:
        n, t = i.split()
        yield WoodChuck(n, int(t))

def prnt(x):
    for i in x:
        print i.name, "the woodchuck can chuck", i.tooth * 5, "kilograms of wood."

wc = list(bld(file("prob3_in.txt")))
wc.sort()
prnt(wc)
