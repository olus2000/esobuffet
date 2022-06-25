#!/usr/bin/python3

# // Code by SoundOfSpouting#6980 (UID: 151149148639330304)
# Supplementary program for interpreter, compiles ordered pairs (a, b)(c, d) or list [1, 2, 3, 4] into raw bytes
# Usage: ./compiler.py [input file] [output file]

import sys;import re;open(sys.argv[2],"wb").write(bytes(map(int,re.sub("[^0123456789\s]","",re.sub("[\[\]{}(),]", " ", open(sys.argv[1],"r").read())).split())))
