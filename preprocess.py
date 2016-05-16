#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print "Using dictionary to replace chinese word @ " + sys.argv[1] 

dictionary = {
        'ㄡ': '喔',
        'ㄛ': '喔',
        'ㄏ': '呵',
        'ㄌ': '了',
        'ㄑ': '去',
        'ㄉ': '的',
        'ㄟ': '欸',
        'ㄋ': '呢',
        'ㄚ': '啊',
        '丫': '呀'
        }


with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    writeList = []
    for line in lines:
        for key, value in dictionary.iteritems():
            if key in line:
                line = line.replace(key, value)
        writeList.append(line)

with open(sys.argv[1][:-5] + "Cut.tsv", 'w') as f:
    print "Writing file " + sys.argv[1][:-5] + "Cut.tsv"
    for line in writeList:
        f.write(line)
