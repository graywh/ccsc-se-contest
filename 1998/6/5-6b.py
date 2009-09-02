#!/usr/bin/env python

import datetime

for line in file('prob6_in.txt', 'r').read().splitlines():
    print (datetime.date(1900 + int(line[:2]), 1, 1) + datetime.timedelta(days=int(line[2:]) - 1)).strftime('%m/%d/%Y')
