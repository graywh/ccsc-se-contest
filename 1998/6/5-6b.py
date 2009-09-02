#!/usr/bin/env python

import sys, datetime

for line in sys.stdin.read().splitlines():
    print (datetime.date(1900 + int(line[:2]), 1, 1) + datetime.timedelta(days=int(line[2:]) - 1)).strftime('%m/%d/%Y')
