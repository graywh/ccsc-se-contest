#!/usr/bin/python
ary = ["0","0","0","0","0","0","0"]
chk = ["1","0","0","0","0","0","1"]
fin = open("prob4.in", "r")
q = []
p = []
while 1:
	line = fin.readline()
	if line == "":
		break
	if line[-1] == "\n":
		line = line[:-1]
	for i in range(len(line)):
		q.append(line[i])
while q != []:
	for i in range(0,7):
		ary[i] = q.pop(0)
	if ary == chk:
		while 1:
			cnt = 0
			for i in range(0,7):
				ary[i] = q.pop(0)
			if ary == chk:
				break
			for i in range(0,7):
				cnt += int(ary[i]) * 2 ** (6 - i)
			p.append(chr(cnt))
print "".join([i for i in p])
