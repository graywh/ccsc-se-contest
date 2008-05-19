import datetime, sys

f = '%m.%d.%Y'

count = int(sys.stdin.readline())
for index in xrange(1,count+1):
    date, days = sys.stdin.readline().split()
    days = int(days)
    m, d, y = date.split('.')
    date = datetime.date(int(y), int(m), int(d))
    rdate = date - datetime.timedelta(days=days)
    sys.stdout.write('%s-day reservations for %s will be available on %s\n' % (days, date.strftime(f), rdate.strftime(f)))
