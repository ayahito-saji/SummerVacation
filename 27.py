#usr/bin/env python3

print("27. 文字列から数字への変換2")

items = [["apple",	200,	38],
		["kiwi",	130,	40],
		["orange",	90,		20],
		["grape",	380,	30],
		["peach",	400,	10],
		["cherry",	300,	5],
		["banana",	80,		36],
		["lemon",	150,	20] ]
		

s = "2,000 620 800 900 300 200 3,500 650"

for i in range(0, len(items)):
	items[i][2] = int(s.split(" ")[i].replace(",",""))
	print(items[i][0].ljust(8)+" "+"{0:4,d}".format(items[i][1])+" "+"{0:6,d}".format(items[i][2])+" "+"{0:7,d}".format(items[i][1] * items[i][2]))