#usr/bin/env python3

print("16. 辞書型への変換")

items = [["apple",	200,	38],
		["kiwi",	130,	40],
		["orange",	90,		20],
		["grape",	380,	30],
		["peach",	400,	10],
		["cherry",	300,	5],
		["banana",	80,		36],
		["lemon",	150,	20] ]

prices = {}
for i in range(0, len(items)):
	prices[items[i][0]] = items[i][1]

print(prices)