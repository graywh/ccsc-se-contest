#!/usr/bin/python
if __name__ == "__main__":
	fin = file("prob6.in", "r")
	cnt = 1
	while 1:
		line = fin.readline()
		if line == "":
			break
		line = line.split()
		bagC = int(line[0])
		cont = int(line[1])
		test = []
		test2 = []
		perc = []
		for i in range(0, cont * 2):
			test.append(int(line[i + 2]))
		for j in range(0, cont):
			test2.append(test[j + cont] / float(test[j]))
			perc.append(0)
		tmp = 0
		while tmp < bagC:
			maxi = 0
			val = 0
			for k in range(0, cont):
				if test2[k] > maxi:
					maxi = test2[k]
					val = k
			if maxi != 0:
				if tmp + test[val] <= bagC:
					tmp += test[val]
					perc[val] = 100
				else:
					perc[val] = (bagC - tmp) * 100 / test[val]
					tmp = bagC
				test2[val] = 0
			else:
				break
		print "Game", cnt
		print "------"
		for q in range(0, cont):
			print "Container %s: %s" % (q + 1, perc[q])
		cnt += 1
