#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

gender_totle = {'0': 0, '1': 0, '2': 0}
prev_key = False
for line in sys.stdin:  # map的时候map中的key会被排序
    line = line.strip()
    data = line.split('\t')
    birthyear = data[0]
    curr_key = birthyear
    gender = data[1]

    # 寻找边界，输出结果
    if prev_key and curr_key != prev_key:  # 不是第一次，并且找到了边界
        print >> sys.stdout, "%s year has female %s and male %s" % (
        prev_key, gender_totle['0'], gender_totle['1'])  # 先输出上一次统计的结果
        prev_key = curr_key
        gender_totle['0'] = 0
        gender_totle['1'] = 0
        gender_totle['2'] = 0  # 清零
        gender_totle[gender] += 1  # 开始计数
    else:
        prev_key = curr_key
        gender_totle[gender] += 1
# 输出最后一行
if prev_key:
    print >> sys.stdout, "%s year has female %s and male %s" % (prev_key, gender_totle['0'], gender_totle['1'])