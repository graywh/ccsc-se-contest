#!/usr/bin/python
class WoodChuck:
	def __init__(self, name, tooth):
		self.name = name
		self.tooth = tooth
		
	def __cmp__(self, wc):
		return cmp(self.tooth,wc.tooth)
		
if __name__ == "__main__":
	fin = file("prob3.in", "r")
	wc = []
	while 1:
		line = fin.readline()
		if line == "":
			break
		if line[-1] == "\n":
			line = line[:-1]
		name, tooth = line.split()
		tooth = int(tooth)
		tmp = WoodChuck(name, tooth)
		wc.append(tmp)
	wc.sort()
	for i in range(0,len(wc)):
		print wc[i].name, "the woodchuck can chuck", wc[i].tooth * 5, "kilograms of wood."

