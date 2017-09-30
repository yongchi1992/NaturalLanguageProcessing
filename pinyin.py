#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import string, re
start = "("
r1 = "(([bpmfdtnlgkhjqxrzcsyw]|(zh)|(ch)|(sh)){1}([iuv]|(ai)|(ei)|(ui)|(ao)|(ou)|(iu)|(uo)|(ua)|(ie)|(ue)|(an)|(en)|(ian)|(iao)|(uai)|(in)|(un)|(ang)|(eng)|(ing)|(ong)|(uan)|(uang)){1})"
r2 = "([bpmfw]o)"
r3 = "(([mdtnlgkhrzcsy]|(zh)|(ch)|(sh))e)"
r4 = "(([bpmfdtnlgkhzcsyw]|(zh)|(ch)|(sh))a)"
r5 = "(er|en|ai|ao|ang|an|ei|ou|)"
tail = ")+\s*$"
r = start + r1 + "|" + r2 + "|" + r3 + "|" + r4 + "|" + r5 + tail



""" 
if re.match(r,"yummy"):
    print "    True"
else:
    print "    False"
"""     

f = open("tokens.txt")
res = file("result.txt","w+")
line = f.readline()
while line:
    s = ""
    s = s + line
    if re.match(r,line):
        print line
        s = s + "    拼音\n"
    else:
        s = s + "    英文\n"
    res.write(s)
    line = f.readline()
    
f.close()
res.close()

