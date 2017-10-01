#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import string

f = open("pinyin.txt")
res = file("PYresultNGram4.txt","w+")
line = f.readline()

while line:
    s = ""
    s = s + line
    
    grade = 0
    pgrade = 0
    ngrade = 0
    wordLen = len(line) - 2
                 
    if wordLen <= 4:
        if line[0:wordLen] in dic4:
            grade = 1
        else:
            grade = -1
    else:
        for i in range(wordLen - 2):
            if line[i : i + 4] in dic4:
                grade += 1
                pgrade += 1
            else:
                grade -= 1
                ngrade += 1
            
    
    if grade <= 0 or wordLen >= 15:
        print line
        s = s + str(grade) + "   " + str(pgrade) + "    " + str(ngrade) + "    PY\n"
    else:
        s = s + str(grade) + "   " + str(pgrade) + "    " + str(ngrade) + "    ENG\n"
    res.write(s)
    line = f.readline()
    
f.close()
res.close()
