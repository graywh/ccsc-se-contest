#!/usr/bin/python
fin = file("prob1.in","r")
i = 1
while 1:
	line = fin.readline()
	if line == "":
		break
	if line[-1] == "\n":
		line = line[:-1]
	a,b = line.split()
	a = int(a)
	b = int(b)
	print "%s X %s = " % (a,b),
	sum = 0
	while a > 0:
		if a % 2:
			print b,
			sum += b
			if a > 1:
				print " + ",
		a /= 2
		b *= 2
	print " = %s" % sum
