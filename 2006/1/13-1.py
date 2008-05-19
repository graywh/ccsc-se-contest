import re, sys

indentifier = re.compile(r'^[a-z_$][\w$]*$', re.I)
process = sys.stdin.read().splitlines()
last = process.index('LAST')
end = process.index('END')
reserved = process[0:last]
for index in xrange(last+1,end):
    sys.stdout.write('%s is %svalid\n' % (process[index],['in',''][indentifier.match(process[index]) is not None and process[index] not in reserved]))
