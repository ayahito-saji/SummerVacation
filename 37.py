#!usr/bin/env python3

import csv

file_opener = open("nagoya201707.csv",'r',encoding='utf-8')

dataReader = csv.reader(file_opener)

max_day = [0,0]
min_day = [0,999]

header = next(dataReader)

for row in dataReader:
	if float(row[2]) > max_day[1]:
		max_day = [int(row[0]),float(row[2])]
	if float(row[3]) < min_day[1]:
		min_day = [int(row[0]),float(row[3])]

print("最高気温が最も高い日:"+str(max_day[0])+"日 "+str(max_day[1])+"℃")
print("最低気温が最も低い日:"+str(min_day[0])+"日 "+str(min_day[1])+"℃")
