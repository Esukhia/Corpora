#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import re
import os


for file in os.listdir('./Regex/input'):
    print(file)
    # check the encoding
    try:
        with codecs.open('./Regex/input/' + file, 'r', 'utf-8') as f:
            current_file = f.read()
    except:
        with codecs.open('./Regex/input/' + file, 'r', 'utf-16') as f:
            current_file = f.read()


    # regex list

    regexes = [
                (r'་ ས་ ', r' ས-P '),
		(r' \S+^ས(་| )སུ(་|\s?) ', r' སུ-i '),
                (r'(་ |་ |\s+)', r' '),
                (r'( ངས།|་ངས།)', r' ས-i །'),
                (r'(་། |། )', r' ། '),
                (r' ངས ', r' ང འིས '),
		(r' (ཀྱི|གི|ཡི|གྱི|གྱིན|ཀྱིན|གིན) ', r' འི '),
		(r' (\S+)འི ', r' \1 འི '),
		(r'( |་)(ཀྱིས|གིས|ཡིས|གྱིས) ', r' འིས '),
		(r' (\S+)(་པས|་བས)(\s+།)', r' \1 ས-i །'),
		(r' ས ', r' འིས '),
                (r' (མ་|མི་)(\S+) ', r' མ-N \2 '),
		(r' (མ-n_མི|མ-N) ', r' མ-N '),
                (r'(་ )', r' '),
                (r' (\S+|\S)་(པ|པོ|བ|མ|མོ|ཚོ|དག|ད|ག|ང|ས|ཡ) ', r' \1 \2-ep '),
		(r' ད །', r' ད-ep '),
		(r' (\S+)(འི|འོ|འམ|འང) ', r' \1 \2 '),
		(r' (\S+)་ན ', r' \1 ན '),		
		(r' (\S+)་(དུ|སུ|རུ|ཏུ|ངུ) ', r' \1 དུ '),
		(r' (ར|-ར|_ར) ', r' ལ '),
		(r' བྱེད ', r' བྱས '),
		(r' (ཅིག|ཤིག) ', r' ཞིག '),
		(r' ཅིང ', r' ཞིང '),
		(r' ཅེས ', r' ཞེས '),
		(r' མེད ', r' མ-N ཡོད '),
		(r' མིན ', r' མ-N ཡིན '),
		(r' (དེ|འདི)་(\S+) ', r' \1 \2 '),
		(r'( \S+| )(ནོ|རོ|གོ|སོ|ངོ|དོ)\s+།', r' འོ །'),
		(r' (ཏུ|སུ|རུ|ངུ) ', r' དུ '),
		(r' ང་རང ', r' ང '),
		(r' (ཁྱོད་རང|ཁྱེད་རང|ཁྱོ) ', r' ཁྱོད '),
		(r' (བཀླགས|བཀླག) ', r' ཀློག '),
		(r' བསྒྲུབས ', r' བསྒྲུབ '),
		(r' (རྒྱབ|བརྒྱབས) ', r' བརྒྱབ ')
              ]


    # apply regexes
    for regex in regexes:
        current_file = re.sub(regex[0], regex[1], current_file)
    
    # output results
    pre = 'Lemmatized_'
    with codecs.open('./Regex/output/'+file, 'w', 'utf-8-sig') as f:
        f.write(current_file)
