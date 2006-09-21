#!/usr/bin/python
if __name__ == "__main__":
	fin = file("prob3.in")
	print "Z  I  M  L  Length\n------------------"
	while 1:
		line = fin.readline()
		if line == "":
			break
		z, i, m, l = line.split()
		z = int(z)
		i = int(i)
		m = int(m)
		l = int(l)
		cnt = 0
		print "%s%s%s%s" % (str(z).ljust(3), str(i).ljust(3), str(m).ljust(3), str(l).ljust(3)),
		start = ((z * l + i) % m)
		l = ((z * l + i) % m)
		if m == 1:
			print "ERROR"
			continue
		else:
			while 1:
				l = ((z * l + i ) % m)
				cnt += 1
				if start == l:
					break
			print cnt
