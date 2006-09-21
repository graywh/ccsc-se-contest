#!/usr/bin/python
x = {".-":'A',
	"-...":'B',
	"-.-.":'C',
	"-..":'D',
	".":'E',
	"..-.":'F',
	"--.":'G',
	"....":'H',
	"..":'I',
	".---":'J',
	"-.-":'K',
	".-..":'L',
	"--":'M',
	"-.":'N',
	"---":'O',
	".--.":'P',
	"--.-":'Q',
	".-.":'R',
	"...":'S',
	"-":'T',
	"..-":'U',
	"...-":'V',
	".--":'W',
	"-..-":'X',
	"-.--":'Y',
	"--..":'Z',
	"*":" "}

import sys
if __name__ == "__main__":
	fin = file("prob2.in", "r")
	while 1:
		line = fin.readline()
		if line == "":
			break
		if line[-1] == "\n":
			line = line[:-1]
		line = line.replace("   ", " * ")
		codes = line.split()
		for code in codes:
			sys.stdout.write(x[code])
