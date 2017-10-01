#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import string


f = open("eng.txt")
dic = {}
line = f.readline()

while line:
    s = re.findall("[a-zA-Z]+",str.lower(line))
    for i in range(len(s)):
        word = s[i]
        wordLen = len(word)
        if wordLen <= 3:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
        else:
            for j in range(wordLen - 3):
                if word[j:j+3] in dic:
                    dic[word[j:j+3]] += 1
                else:
                    dic[word[j:j+3]] = 1
    line = f.readline()
