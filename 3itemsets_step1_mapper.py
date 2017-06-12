#!/usr/bin/env python

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split('\t')
	# printing the words as they are  in the input
	print('%s\t%s' % (words[0], words[1]))