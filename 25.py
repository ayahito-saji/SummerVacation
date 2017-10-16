#usr/bin/env python3

print("25. 数字の連結")

items = [["apple",	200,	38],
		["kiwi",	130,	40],
		["orange",	90,		20],
		["grape",	380,	30],
		["peach",	400,	10],
		["cherry",	300,	5],
		["banana",	80,		36],
		["lemon",	150,	20] ]

unit_prices = ""
for i in range(0, len(items)):
	unit_prices += str(items[i][1])+","
unit_prices = unit_prices[:-1]
print(unit_prices)