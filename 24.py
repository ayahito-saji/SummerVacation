#usr/bin/env python3

print("24. 文字列の連結")

items = [["apple",	200,	38],
		["kiwi",	130,	40],
		["orange",	90,		20],
		["grape",	380,	30],
		["peach",	400,	10],
		["cherry",	300,	5],
		["banana",	80,		36],
		["lemon",	150,	20] ]

names = ""
for i in range(0, len(items)):
	names += items[i][0]+","
names = names[:-1]
print(names)