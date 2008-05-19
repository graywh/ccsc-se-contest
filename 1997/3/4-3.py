#!/usr/bin/python
class WoodChuck:
    def __init__(self, name, tooth):
        self.name = name
        self.tooth = tooth
        
    def __cmp__(self, wc):
        return cmp(self.tooth,wc.tooth)
        
if __name__ == "__main__":
    wc = []
    for line in file("prob3.in", "r").read().splitlines():
        name, tooth = line.split()
        tooth = int(tooth)
        tmp = WoodChuck(name, tooth)
        wc.append(tmp)
    wc.sort()
    for i in xrange(len(wc)):
        print wc[i].name, "the woodchuck can chuck", wc[i].tooth * 5, "kilograms of wood."
