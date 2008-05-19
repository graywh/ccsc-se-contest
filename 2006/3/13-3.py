import sys, math

count = int(sys.stdin.readline().split()[0])
for index in xrange(1,count+1):
    sys.stdout.write('Booklet %s:  \n' % (index))
    pages = int(sys.stdin.readline().split()[0])
    f = int(math.ceil(pages / 4.))
    n = map(str, range(1, pages+1))
    n.extend('-' * (4 * f - pages))
    map(lambda i: sys.stdout.write('Folio %s:  %s\n' % (i, ' '.join([n[f*2-i*2+1],n[f*2+i*2-2],n[f*2+i*2-1],n[f*2-i*2]]))), xrange(1,f+1))
    sys.stdout.write('\n')
