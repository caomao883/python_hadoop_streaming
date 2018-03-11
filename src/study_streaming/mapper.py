#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

for line in sys.stdin:
    line = line.strip()
    data = line.split(',')
    if len(data)<3:
        continue
    user_id = data[0]
    birthyear = data[1][0:4]
    gender = data[2]
    print >>sys.stdout,"%s\t%s"%(birthyear,gender)