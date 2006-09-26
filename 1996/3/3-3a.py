#!/usr/bin/python
symbols = ("&", ".", ",", ":", ";", "?", "!", "-", "(", ")")

if __name__ == "__main__":
	fin = file("words.txt", "r")
	lines = fin.readlines()
	cnt = 0
	for line in lines:
		for symbol in symbols:
			line = line.replace(symbol, "")
		cnt += len(line.split())
	print "This file contains %s words." % cnt
