#!/usr/bin/python
class PTree:
	class Node:
		def __init__(self, d):
			self.data = d
			self.left = None
			self.right = None

	def __init__(self, fin):
		self.isPalin = 0
		self.pal = ""
		self.root = self.create(fin)
		s = ""
		self.traverseAll(self.root, s)

	def isPal(self):
		return self.isPalin

	def getPal(self):
		return self.pal

	def create(self, fin):
		fin.pop(0)
		ch = fin.pop(0)
		if ch == ")":
			return None
		tmp = PTree.Node(ch)
		tmp.left = self.create(fin)
		tmp.right = self.create(fin)
		fin.pop(0)
		return tmp

	def traverseAll(self, n, s):
		s = s + str(n.data)
		if n.left == None and n.right == None:
			self.isPalin = self.isPalindrome(s)
		if self.isPalin:
			self.pal = s
		if n.left != None and not self.isPalin:
			self.traverseAll(n.left, s)
		if n.right != None and not self.isPalin:
			self.traverseAll(n.right, s)

	def isPalindrome(self, s):
		for i in range(0, len(s) - 1):
			if s[i] != s[-i - 1]:
				return 0
		return 1

if __name__ == "__main__":
	fin = file("prob3.in", "r")
	cnt = 1
	while 1:
		line = fin.readline()
		if line == "":
			break
		if line[-1] == "\n":
			line = line[:-1]
		ln = []
		for i in range(0, len(line)):
			ln.append(line[i])
		t = PTree(ln)
		print "Tree %s is" % cnt,
		if t.isPal():
			print "a palintree. Its palintree is %s." % t.getPal()
		else:
			print "not a palintree."
		cnt += 1