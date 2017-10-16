#!usr/bin/env python3

import csv
import numpy as np
import matplotlib.pyplot as plt

files = ["nagoya201707.csv","irago201707.csv","inabu201707.csv"]
place = ["Nagoya","Irago","Inabu"]
data = []
for i in range(3):
	data.append([])
	file_opener = open(files[i],'r',encoding='utf-8')
	dataReader = csv.reader(file_opener)
	header = next(dataReader)
	for row in dataReader:
		data[i].append(float(row[1]))

left = [i for i in range(len(data[0]))]

plt.title("Daily Mean Temperature on July, 2017")
plt.xlabel("Date")
plt.ylabel("Mean Air Temperature")
p0 = plt.plot(left, data[0], label=place[0], linewidth=2)
p1 = plt.plot(left, data[1], label=place[1], linewidth=2)
p2 = plt.plot(left, data[2], label=place[2], linewidth=2)
plt.legend(loc=2)
plt.show()