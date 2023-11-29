#!/usr/bin/python3

number = set()
for i in range(0, 99):
	covert = str(i)
	sorted_num = ''.join(sorted(number))
	number.add(i)
	if covert in number:
		continue
