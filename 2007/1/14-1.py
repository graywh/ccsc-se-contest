import sys

ups = {
        '0': '0',
        '1': '1',
        '2': '2',
        '3': 'x',
        '4': 'x',
        '5': '5',
        '6': '9',
        '7': 'x',
        '8': '8',
        '9': '6',
        }

sys.stdin.readline()
lines = sys.stdin.read().splitlines()

for l in lines:
    c = [ups[x] for x in l]
    c.reverse()
    c = ''.join(c)
    print "%s:" % l,
    if c == l:
        print "Yes"
    else:
        print "No"
