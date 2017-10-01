#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:31:17 2017

@author: yongchizhang
"""

import re
# regular expression

sdd="lvnvv"
if re.match("([ln]v)+$",sdd):
    print "right"
else:
    print "wrong"