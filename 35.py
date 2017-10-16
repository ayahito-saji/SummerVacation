#usr/bin/env python3

import re

print("35. 単語の出現回数")

file_opener = open("constitution.txt",'r')

dic = {}
def addWord(word):
	if(word in dic):
		dic[word] += 1
	else:
		dic[word] = 1

for line_data in file_opener:
	line_data = line_data.strip()
	words = re.split("\s|\,|\.|\(|\)",line_data.lower())
	for i in range(0, len(words)):
		if words[i] != "":
			addWord(words[i])

list = []
for key in dic.keys():
	list.append([key,dic[key]])

list = sorted(list, key=lambda x: x[1])
list.reverse()

for i in range(0,len(list)):
	print(list[i][0]+" : "+str(list[i][1]))