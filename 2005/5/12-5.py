import sys

for i in sys.stdin.read().splitlines()[1:]:
    problem = map(int, sys.stdin.readline().split())
    print 1 - problem[0] + sum(problem[1:])
