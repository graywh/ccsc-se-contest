#!/usr/bin/python
if __name__ == "__main__":
	fin = file("prob6.in", "r")
	cnt = 1
	while 1:
		line = fin.readline()
		if line == "":
			break
		ln = line.split()
		caproom = int(ln[0])
		n = int(ln[1])
		conts = []
		for i in range(0, n):
			conts.append(int(ln[i + 2]))
		conts.sort()
		conts.reverse()
		ship = []
		while caproom >= conts[-1]:
			ship.append(conts[-1])
			caproom -= conts.pop()
		if caproom > 0:
			for i in conts:
				for j in ship:
					if caproom + j >= i and j <= i:
						caproom += j
						caproom -= i
						j = i
		print
		print "Ship", cnt
		print "------"
		print "Number of containers loaded:", len(ship)
		print "Weight under capacity:", caproom
		cnt += 1
