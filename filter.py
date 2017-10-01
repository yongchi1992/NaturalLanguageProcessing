#!/usr/bin/env python2
# -*- coding: utf-8 -*-

total = 0
n = 0
for key in dic:
    total += dic[key]
    n += 1
avg = total / n

keys = list(dic.keys())
for key in keys:
    if dic[key] < 15:
        del dic[key]
        
        
keys = list(dic4.keys())
for key in keys:
    if dic4[key] < 15:
        del dic4[key]