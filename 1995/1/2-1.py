#!/usr/bin/python
i = 1
for line in file('prob1.in', 'r').read().splitlines():
	a,b = map(int, line.split())
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
