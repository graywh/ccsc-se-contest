import sys

order = {
            4: 0,
            8: 1,
            3: 2,
            7: 3,
            2: 4,
            6: 5,
            1: 6,
            5: 7,
        }

steps = [
            "up",
            "down",
        ]

sys.stdin.readline()

lines = sys.stdin.read().splitlines()

for i,l in enumerate(lines):
    print "Case %s:" % (i+1),
    f, t = [order[int(x)] for x in l.split()]
    if f < t:
        for j in xrange(f, t):
            print steps[j % 2],
        print
    else:
        print "Take the stairs!"
