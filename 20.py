#usr/bin/env python3

print("20. 辞書型からリストへの変換と比較")

items = [["apple",	200,	38],
		["kiwi",	130,	40],
		["orange",	90,		20],
		["grape",	380,	30],
		["peach",	400,	10],
		["cherry",	300,	5],
		["banana",	80,		36],
		["lemon",	150,	20] ]

sales = {'kiwi': (130, 40), 'grape': (380, 30), 'apple': (200, 38), 'peach': (400, 10), 'cherry': (300, 5), 'orange': (90, 25), 'lemon': (160, 20), 'banana': (80, 36)}

itemsFromSales = []
for each_key in sales.keys():
	itemsFromSales.append([each_key, sales[each_key][0], sales[each_key][1]]);

items = sorted(items, key=lambda x: x[0])
itemsFromSales = sorted(itemsFromSales, key=lambda x: x[0])
for i in range(0,len(items)):
	if(items[i][1] != itemsFromSales[i][1] or items[i][2] != itemsFromSales[i][2]):
		print(str(items[i])+" "+str(itemsFromSales[i]))