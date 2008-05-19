import sys

insig = []
for line in sys.stdin.read().splitlines()[:-1]:
    amt, unit, dv, name = line.split(' ', 3)
    pct = int(float(amt) / float(dv) * 100)
    if pct == 0:
        insig.append(name)
    else:
        sys.stdout.write('%s %s %s %s%%\n' % (name, amt, unit, pct))
sys.stdout.write('Provides no significant amount of:\n%s' % ('\n'.join(insig)))
