#!/usr/bin/env python

import sys

current_word = None
word = None
for line in sys.stdin:
	line = line.strip()
	word, value = line.rsplit('\t', 1)
	if current_word == word:
		values.append(value)
	else:
		#check if the candidate is frequent, in which case freq will be in values. Only then, we print.
		if current_word and 'freq' in values:
			values.remove('freq')
			current_word=current_word.split('\t')
			current_word = list(map(int, current_word))
			current_word.sort()
			for each_value in values:
				print('%s\t%s\t%s' % (each_value, current_word[0],current_word[1]))
		values=[]
		values.append(value)
		current_word = word
# do not forget to output the last word if needed!
if current_word == word and 'freq' in values:
	values.remove('freq')
	current_word=current_word.split('\t')
	current_word = list(map(int, current_word))
	current_word.sort()
	for each_value in values:
		print('%s\t%s\t%s' % (each_value, current_word[0],current_word[1]))
