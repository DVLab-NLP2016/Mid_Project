#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print "Using dictionary to replace chinese word @ " + sys.argv[1] 

dictionary = {
        # Replacement
        'ㄅ': '',
        'ㄆ': '跑',
        'ㄇ': '麼',
        'ㄎ': '呵',
        'ㄡ': '喔',
        'ㄛ': '喔',
        'ㄏ': '呵',
        'ㄌ': '',
        'ㄑ': '去',
        'ㄉ': '',
        'ㄟ': '欸',
        'ㄋ': '呢',
        'ㄚ': '啊',
        '丫': '呀',
        'ㄍ': '',
        # Stop Words
        '的': '', 
        "了": '', 
        "在": '', 
        "是": '', 
        "我": '', 
        "有": '', 
        "和": '', 
        "就": '',  
        "不": '', 
        "人": '', 
        "都": '', 
        "一": '', 
        "一個": '', 
        "上": '', 
        "也": '', 
        "很": '', 
        "到": '', 
        "說": '', 
        "要": '', 
        "去": '', 
        "你": '',          
        "會": '', 
        "著": '', 
        "沒有": '', 
        "看": '', 
        "好": '', 
        "自己": '', 
        "這": '', 
        # Removement
        '：': '',
        '。': '',
        '，': '',
        '～': '',
        '「': '',
        '」': '',
        '〝': '',
        '〞': '',
        '．': '',
        '、': '',
        '？': '',
        '！': '',
        '※': '',
        '?': '',
        '!': '',
        '…': ''
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
