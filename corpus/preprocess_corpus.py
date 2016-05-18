#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

threshold = 8
removeList = []
with open(sys.argv[1], 'r') as f:
    print "Processing " + sys.argv[1]
    lines = f.readlines()
    for line in lines:
        s = line.split()
        index = 0
        for element in s:
            # Removing not chinese word
            if not (u'\u4e00' <= element.decode('utf-8') <= u'\u9fff') and not element.startswith('EMOTICON'):
                s.remove(element)
                break
        for element in s:
            if element.startswith('EMOTICON'):
                index = s.index(element)
                break
        left = index - threshold
        if left < 0:
            left = 0
        right = index + threshold
        if right >= len(s):
            right = len(s)
        subS = s[left:right]
        subString = ""
        for subs in subS:
            subString += subs
            subString += ' '
        removeList.append(subString+'\n')

with open(sys.argv[1][:-4] + '-remove.txt', 'w') as f:
    print "Writing removed file"
    for line in removeList:
        f.write(line)
