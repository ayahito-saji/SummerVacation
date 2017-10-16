#usr/bin/env python3

import re

import numpy as np
import matplotlib.pyplot as plt

print("36. 棒グラフの表示")

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

X = []
Y = []
Z = []
for i in range(50):
	X.append(i)
	Y.append(list[i][1])
	Z.append(list[i][0])

plt.bar(X, Y)
plt.xticks(X, Z, rotation = 90)
plt.show()