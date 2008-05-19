#!/usr/bin/python
if __name__ == "__main__":
	fin = file("prob3.in", "r")
	channel = 1
	while 1:
		line = fin.readline()
		if line == "":
			break
		line = line.split()
		ary = []
		for i in line:
			ary.append(int(i))
		cross = 0
		for i in xrange(1, len(ary)):
			for j in xrange(i):
				if ary[i] < ary[j]:
					cross += 1
		print "There are %s wire crossins in routing channel %s." % (cross, channel)
		channel += 1
