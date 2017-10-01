#!/usr/bin/env python2
# -*- coding: utf-8 -*-

line = "abbye"
grade = 0
wordLen = 5
             
if wordLen <= 3:
    if line[0:wordLen] in dic:
        grade = 1
    else:
        grade = -1
else:
    for i in range(wordLen - 2):
        if line[i : i + 3] in dic:
            grade += 1
        else:
            grade -= 1
