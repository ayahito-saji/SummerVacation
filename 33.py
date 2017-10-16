#usr/bin/env python3

import re

print("33. 単語マッチ")

file_opener = open("constitution.txt",'r')

for line_data in file_opener:
	line_data = line_data.strip()
	if re.search(r"(\W+|^)((l|L)aws?|LAWS?)(\W+|$)",line_data):
		print(line_data)