#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re
import os

for file in os.listdir('D:/Corpora/python/Regex/input'):
    # print(file.encode("utf-8-sig"))
    # check the encoding
    try:
        with codecs.open('D:/Corpora/python/Regex/input/' + file, 'r', 'utf-8') as f:
            current_file = f.read()
    except:
        with codecs.open('D:/Corpora/python/Regex/input/' + file, 'r', 'utf-16') as f:
            current_file = f.read()

    # regex list
    regexes = [
                
                (r'\s*་*\s*།\s*', r' ། '),
                (r'(\s*་*\s+)', r' ')

              ]

    # apply regexes
    for regex in regexes:
        current_file = re.sub(regex[0], regex[1], current_file)
    
    # output results
    pre = 'un-tsheged_'
    with codecs.open('D:/Corpora/python/Regex/output/' + file, 'w', 'utf-8-sig') as f:
        f.write(current_file)
