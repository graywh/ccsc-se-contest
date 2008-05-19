import sys, math

lines = sys.stdin.read().splitlines()
count = int(lines[0])
for index in xrange(1,count+1):
    a,b = lines[index].split()
    c = int(a,2) + int(b,2)
    out = []
    for i in xrange(int(math.floor(math.log(c,2))), -1, -1):
        out.append(str(c / 2**i))
        c = c % 2**i
    sys.stdout.write('%s %s\n' % (index, ''.join(out)))
