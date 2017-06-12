#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split('\t')
	# If there are more than 2 elements in a line, it is output of previous step
	if len(words)>2:
		key=words.pop()
	# If there are 2 elements in a line, it is output of 2 freq itemset
	else:
		key='freq'
	words.sort()
	try:
		print('%s\t%s\t%s' % (words[0], words[1], key))
	except:
		continue