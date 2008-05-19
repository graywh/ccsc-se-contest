#!/usr/bin/python
def oper(pos, pre):
	q = 0
	print "(",
	if ord(pre[pos + 1 + q]) >= ord('0') and ord(pre[pos + 1 + q]) <= ord('9'):
		print pre[pos + 1 + q],
	else:
		q += oper(pos + 1 + q, pre)
	print pre[pos],
	if ord(pre[pos + 2 + q]) >= ord('0') and ord(pre[pos + 2 + q]) <= ord('9'):
		print pre[pos + 2 + q],
	else:
		q += oper(pos + 2 + q, pre)
	print ")",
	return q + 2
	
if __name__ == "__main__":
	fin = file("prob5.in")
	while 1:
		pre = fin.readline()
		if pre == "":
			break
		if ord(pre[0]) >= ord('0') and ord(pre[0]) <= ord('9'):
			print pre[0],
		else:
			oper(0, pre)
		print
