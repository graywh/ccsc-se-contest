#!/usr/bin/python
def parse(line):
	ch = line[0]
	line = line[1:]
	d = ord(ch)
	if d >= ord('0') and d <= ord('9'):
		print ch,
	else:
		print "(",
		line = parse(line)
		print ch,
		line = parse(line)
		print ")",
	return line

if __name__ == "__main__":
	fin = file("prob5.in")
	while 1:
		line = fin.readline()
		if line == "":
			break
        line = parse(line)
		print
