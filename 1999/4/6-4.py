#!/usr/bin/python
if __name__ == "__main__":
	fin = file("prob4.in", "r")
	while 1:
		line = fin.readline()
		if line == "":
			break
		dim = line.split()
		dim = int(dim[0])
		diag = 0
		magic = 1
		grid = [0] * (dim + 1)
		for i in range(0, dim):
			line = fin.readline()
			line = line.split()
			g = [None] * (dim + 1)
			for j in range(0, dim):
				g[j] = int(line[j])
			g[-1] = 0
			grid[i] = g
		grid[-1] = [0] * (dim + 1)
		for i in range(0, dim):
			grid[dim][dim] += grid[i][i]
			diag += grid[dim - i - 1][i]
			for j in range(0, dim):
				grid[i][dim] += grid[i][j]
				grid[dim][j] += grid[i][j]
		for i in range(0, dim):
			if grid[i][dim] != diag:
				magic = 0
			if grid[dim][i] != diag:
				magic = 0
		if grid[dim][dim] != diag:
			magic = 0
		if magic:
			print "HOCUS"
		else:
			print "POCUS"
