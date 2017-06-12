#!/usr/bin/env python

import sys

current_word = None
word = None
support=1000
# input comes from STDIN

for line in sys.stdin:
	line = line.strip()
	word, value = line.split('\t', 1)
	if current_word == word:
		# storing all values for a particular key
		values.append(int(value))
	else:
		if current_word:
			# sorting values before printing to maintain order
			values.sort()
			for i in range(len(values)):
				j = i + 1
				while (j < len(values)):
					try:
						print('%s\t%s\t%s' % (values[i], values[j],current_word))
						j += 1
					except:
						continue
		# values will be initialized as an empty list here for every unique key
		values=[]
		values.append(int(value))
		current_word = word
# do not forget to output the last word if needed!
if current_word == word:
	values.sort()
	for i in range(len(values)):
		j = i + 1
		while (j < len(values)):
			try:
				print('%s\t%s\t%s' % (values[i], values[j],current_word))
				j += 1
			except:
				continue