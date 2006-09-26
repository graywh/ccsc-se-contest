#!/usr/bin/python
if __name__ == "__main__":
	fin = file("buffy.dat", "r")
	msg = 1
	while 1:
		line = fin.readline()
		if line == "":
			break
		if line[-1] == "\n":
			line = line[:-1]
		rows,cols = line.split()
		rows = int(rows)
		cols = int(cols)
		ary = []
		for i in range(0,rows):
			ln = []
			line = fin.readline()
			ln = line.split()
			ary.append(ln)
		print "Message", msg, "=>",
		j = cols - 1
		for i in range(0,rows):
			print ary[i][j],
			j -= 1
			if j < 0:
				j = cols - 1
		print
		msg += 1
