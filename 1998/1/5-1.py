#!/usr/bin/python
class Node:
	def __init__(self, v = " "):
		self.val = v
		self.child = []

def match(name = "", n = 1, names = [], bill = []):
	name += bill[n - 1].val
	if bill[n - 1].child == []:
		names.append(name)
	else:
		for i in xrange(len(bill[n - 1].child)):
			match(name, bill[n - 1].child[i], names, bill)

if __name__ == "__main__":
	fin = file("prob1.in", "r")
	cnt = 1
	while 1:
		line = fin.readline()
		if line == "":
			break
		if line[-1] == "\n":
			line = line[:-1]
		names = []
		num, m, v = line.split()
		num = int(num)
		m = int(m)
		bill = [None] * num
		bill[0] = Node(v)
		for i in xrange(m):
			line = fin.readline()
			p, num, s, v = line.split()
			p = int(p)
			num = int(num)
			bill[num - 1] = Node(v)
			bill[p - 1].child.append(num)
		match("", 1, names, bill)
		full = 1
		part = 0
		for name in names:
			if name != names[0]:
				full = 0
			if names.count(name) > 1:
				part = 1
		print "Sample %s:" % cnt,
		if full == 1:
			print "Exact match - summon the grand jury."
		elif part == 1:
			print "Partial match - close, but no cigar."
		else:
			print "No match - sorry, Ken."
		cnt += 1
		
