#!/usr/bin/python
trash = [",", ".", "!", "?", "\n", ":", ";"]
swap = ["Th", "Kh", "Wh", "Tr", "Sh", "Fl", "th", "kh", "wh", "tr", "sh", "fl"]

if __name__ == "__main__":
	fin = file("pig.dat", "r")
	while 1:
		line = fin.readline()
		if line == "":
			break
		words = line.split()
		for word in words:
			end = ""
			for trsh in trash:
				if word[-1] == trsh:
					word = word[:-1]
					end = trsh
					break
			word = word[:-2]
			done = 0
			for swp in swap:
				if word[-2:] == swp:
					word = swp + word[:-2]
					done = 1
					break
			if done == 0:
				if word[-1] == "y":
					word = word[:-1]
				else:
					word = word[-1] + word[:-1]
			print "%s%s" % (word, end),
