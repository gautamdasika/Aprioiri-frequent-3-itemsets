#!/usr/bin/env python

import sys
import re
f=open("candidates","r")
content=f.read().splitlines()
f.close()
# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split(' ')
	words=set(words)
	for candidate in content:
		split_cand=candidate.split('\t')
		# print all candidates that are subsets of the current transaction
		if set(split_cand)<words:
			print('%s\t%s' % (candidate, 1))