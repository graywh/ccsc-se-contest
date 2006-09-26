#!/usr/bin/python
if __name__ == "__main__":
	fin = file("mono.in", "r")
	while 1:
		line = fin.readline()
		if line == "":
			break
		if line[-1] == "\n":
			line = line[:-1]
		mono = 1
		up = line[0] < line[1]
		for i in range(len(line) - 1):
			if up and line[i] >= line[i + 1] or not up and line[i] <= line[i + 1]:
				mono = 0
		if mono == 1:
			print line
