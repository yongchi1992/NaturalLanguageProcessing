#!/usr/bin/env python2
# -*- coding: utf-8 -*-

engtotal = file("englishTotal.txt","w+")
f1 = open("english.txt")
f2 = open("PYresultNGram.txt")

line = f1.readline()

while line:
    engtotal.write(line)
    line = f1.readline()
    
f1.close()

line = f2.readline()

count = 0
while line:
    if count % 2 == 0:
        word = line
    else:
        if "ENG" in line:
            engtotal.write(word)
    line = f2.readline()
    count += 1