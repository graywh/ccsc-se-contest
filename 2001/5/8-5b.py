#!/usr/bin/python
if __name__ == "__main__":
	fin = file("prob5.in")
	mem = []
	extra = 0
	while 1:
		line = fin.readline()
		if line == "":
			break
		if line[-1] == "\n":
			line = line[:-1]
		cont = 0
		for i in xrange(len(line)):
			ch = line[i]
			if cont:
				cont -= 1
				continue
			if ord(ch) >= ord('0') and ord(ch) <= ord('9'):
				print ch,
				while len(mem) and ord(line[i + 1]) >= ord('0') and ord(line[i + 1]) <= ord('9'):
					print mem.pop(0),line[i + 1],")",
					i += 1
					cont += 1
				if len(mem) and i < len(line):
					print mem.pop(0),
					extra += 1
			else:
				print "(",
				mem.append(ch)
		for i in xrange(extra):
			print ")",
		print
