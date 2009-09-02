#!/usr/bin/env python

import sys

def oper(pos, pre):
    q = 0
    sys.stdout.write("(")
    if ord(pre[pos + 1 + q]) >= ord('0') and ord(pre[pos + 1 + q]) <= ord('9'):
        sys.stdout.write(pre[pos + 1 + q])
    else:
        q += oper(pos + 1 + q, pre)
    sys.stdout.write(' ' + pre[pos] + ' ')
    if ord(pre[pos + 2 + q]) >= ord('0') and ord(pre[pos + 2 + q]) <= ord('9'):
        sys.stdout.write(pre[pos + 2 + q])
    else:
        q += oper(pos + 2 + q, pre)
    sys.stdout.write(")")
    return q + 2

for pre in sys.stdin:
    if pre == "":
        break
    if ord(pre[0]) >= ord('0') and ord(pre[0]) <= ord('9'):
        sys.stdout.write(pre[0])
    else:
        oper(0, pre)
    print
