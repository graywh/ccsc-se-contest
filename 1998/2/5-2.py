#!/usr/bin/python
def clear(grid, dim, x, y):
    grid[x][y] = 0
    for i in xrange(-1,2):
        for j in xrange(-1,2):
            if x+i in dim and y+j in dim and grid[x+i][y+j]:
                clear(grid, dim, x + i, y + j)

if __name__ == "__main__":
    fin = file("prob2.in", "r")
    targets = 0
    dim = xrange(int(fin.readline()))
    grid = map(lambda x: map(int, x), map(list, fin.read().splitlines()))
    #print "\n".join([str(k) for k in grid])
    for i in dim:
        for j in dim:
            if grid[i][j]:
                targets += 1
                clear(grid, dim, i, j)
    print "There are %s targets in the current image." % targets
