#!/usr/bin/python
if __name__ == "__main__":
	fin = file("prob2.in")
	while 1:
		line = fin.readline()
		if line == "" or line == "\n":
			break
		numcoins = line.split()
		numcoins = int(numcoins[0])
		p1 = []
		p2 = []
		worst = numcoins * (numcoins + 1) / 4
		best = numcoins * (numcoins + 1) / 2 - worst
		sum1 = 0
		sum2 = 0
		for i in range(numcoins,0,-1):
			if sum1 + i <= best:
				sum1 += i
				p1 = [i] + p1
			else:
				sum2 += i
				p2 = [i] + p2
		print
		print "Number of coins:", numcoins
		print "Pile 1 contains",
		print ", ".join([str(i) for i in p1]),
		print "with value %s." % sum1
		print "Pile 2 contains",
		print ", ".join([str(i) for i in p2]),
		print "with value %s." % sum2
