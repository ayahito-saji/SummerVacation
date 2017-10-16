#!usr/bin/env python3

import csv

files = ["nagoya201707.csv","irago201707.csv","inabu201707.csv"]
place = ["名古屋","伊良湖","稲武"]
data = []
for i in range(3):
	data.append([])
	file_opener = open(files[i],'r',encoding='utf-8')
	dataReader = csv.reader(file_opener)
	header = next(dataReader)
	for row in dataReader:
		data[i].append(float(row[2]))

for i in range(len(data[0])):
	max_place = -1
	if data[0][i] >= data[1][i] and data[0][i] >= data[2][i]:
		max_place = 0
	if data[1][i] >= data[2][i] and data[1][i] >= data[0][i]:
		max_place = 1
	if data[2][i] >= data[0][i] and data[2][i] >= data[1][i]:
		max_place = 2
	print(str(i+1)+"日 "+place[max_place]+" "+str(data[max_place][i])+"℃")