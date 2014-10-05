#!/usr/bin/env python3
# usage: compile-scope.py myscore.tabc

import sys
import os.path
import re

if (len(sys.argv) == 1) or (sys.argv[1] == '-h'):
   print('usage: compile-scope.py myscore.tabc\n(outputs myscore.tex)')

filename = sys.argv[1]
outfilename = os.path.splitext(filename)[0] + '.tex'

with open (filename, "r") as myfile:
    data=myfile.read()

data = re.sub('//.*\n', '', data)
data = re.sub('\n', '', data)
data = re.sub('<1:([^>]*)>', '\\\\meaningful{\\1}', data)
data = re.sub('<2:([^>]*)>', '\\\\fixedintercal{\\1}', data)
data = re.sub('<3:([^>]*)>', '\\\\varintercal{\\1}', data)
data = re.sub('<4:([^>]*)>', '\\\\opener{\\1}', data)
data = re.sub('<5:([^>]*)>', '\\\\prolonger{\\1}', data)
data = re.sub('\\(([^)]*)\\)', '\\\\neume{\\1}', data)
data = re.sub('([ༀ-༃ཀ-ྼ]*)([࿁࿀])', '\\\\centerds{\\1}{\\2}', data)

with open(outfilename, "w") as text_file:
    text_file.write(data)
