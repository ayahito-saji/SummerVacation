#usr/bin/env python3

import re

print("34. 単語数")

file_opener = open("constitution.txt",'r')

count = 0
for line_data in file_opener:
	line_data = line_data.strip()
	words = re.split("\s|\,|\.|\(|\)",line_data)
	for i in range(0, len(words)):
		if words[i] != "":
			count += 1
print(count)