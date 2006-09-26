#!/usr/bin/python
class Point:
	def __init__(self):
		self.x = 0.0
		self.y = 0.0

def distance(a, b):
	return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5

if __name__ == "__main__":
	fin = file("prob5.in")
	cnt = 1
	while 1:
		line = fin.readline()
		if line == "":
			break
		ships = line.split()
		ships = int(ships[0])
		plot = []
		for i in range(0, ships):
			line = fin.readline()
			line = line.split()
			pt = Point()
			pt.x = float(line[0])
			pt.y = float(line[1])
			plot.append(pt)
		mini = distance(plot[0], plot[1])
		n1 = 0
		n2 = 1
		for i in range(0, ships - 1):
			for j in range(i + 1, ships):
				tmp = distance(plot[i], plot[j])
				if tmp < mini:
					mini = tmp
					n1 = i
					n2 = j
		print "Fleet %s: Ship %s and Ship %s are the closeest pair." % (cnt, n1 + 1, n2 + 1)
		cnt += 1
