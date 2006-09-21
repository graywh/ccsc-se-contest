#!/usr/bin/python
if __name__ == "__main__":
	fin = file("prob3.in", "r")
	ln = 1
	while 1:
		line = fin.readline()
		if line == "":
			break
		if line[-1] == "\n":
			line = line[:-1]
		nofreqs = 1
		cnt = 0
		freq = [0] * 26
		for ch in line:
			ch = ch.lower()
			i = ord(ch)
			if ch <= "z" and ch >= "a":
				freq[i - ord("a")] += 1
			cnt += 1
		print "Line %s: " % ln,
		for i in range(0,26):
			if 20 * freq[i] > 3 * cnt:
				print chr(i + ord("A")), "is a super freq.",
				nofreqs = 0
		if nofreqs:
			print "There are no super freqs.",
		print
		ln += 1
