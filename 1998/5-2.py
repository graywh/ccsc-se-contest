#!/usr/bin/python
def clear(grid, x, y):
	grid[x][y] = 0
	for i in range(-1,2):
		for j in range(-2,2):
			if grid[x + i][y + j]:
				clear(grid, x + i, y + j)

if __name__ == "__main__":
	fin = file("prob2.in", "r")
	targets = 0
	line = fin.readline()
	dim = int(line)
	grid = [0] * (dim + 2)
	grid[0] = [0] * (dim + 2)
	for i in range(1,dim + 1):
		line = fin.readline()
		l = [0] * (dim + 2)
		for j in range(1, dim + 1):
			l[j] = int(line[j - 1])
		grid[i] = l
	grid[dim + 1] = [0] * (dim + 2)
	#print "\n".join([str(k) for k in grid])
	for i in range(1,dim + 1):
		for j in range(1, dim + 1):
			if grid[i][j]:
				targets += 1
				clear(grid, i, j)
	print "There are %s targets in the current image." % targets
