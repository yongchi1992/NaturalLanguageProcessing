#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import string


f = open("eng.txt")
dic4 = {}
line = f.readline()

while line:
    s = re.findall("[a-zA-Z]+",str.lower(line))
    for i in range(len(s)):
        word = s[i]
        wordLen = len(word)
        if wordLen <= 4:
            if word in dic4:
                dic4[word] += 1
            else:
                dic4[word] = 1
        else:
            for j in range(wordLen - 4):
                if word[j:j+4] in dic4:
                    dic4[word[j:j+4]] += 1
                else:
                    dic4[word[j:j+4]] = 1
    line = f.readline()
