#usr/bin/env python3

print("19. 複雑な割引")

items = [["apple",	200,	38],
		["kiwi",	130,	40],
		["orange",	90,		20],
		["grape",	380,	30],
		["peach",	400,	10],
		["cherry",	300,	5],
		["banana",	80,		36],
		["lemon",	150,	20] ]

sales = {}
for i in range(0, len(items)):
	sales[items[i][0]] = (items[i][1], items[i][2])

for each_key in sales.keys():
	price = sales[each_key][0] * sales[each_key][1]
	if sales[each_key][1]>= 30:
		price *= 0.9
	if sales[each_key][1]>= 10 and (each_key == "peach" or each_key == "cherry"):
		price *= 0.9
	price *= 1.08
	print(each_key.ljust(8)+" "+"{0:5d}".format(int(price)))