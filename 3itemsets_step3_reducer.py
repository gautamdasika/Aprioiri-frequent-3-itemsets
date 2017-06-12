#!/usr/bin/env python

import sys

current_word = None
current_count = 0
word = None
support=1000
# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	word, count = line.rsplit('\t', 1)

	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	if current_word == word:
		current_count += count
	else:
		# prune candidates that do not satisfy the support condition
		if current_word and current_count>support:
			# write result to STDOUT
			print('%s' % (current_word))
		current_count = count
		current_word = word

# do not forget to output the last word if needed!
if current_word == word and current_count>support:
	print('%s' % (current_word))