#usr/bin/env python3

print("13. 小計の表示")

items = [["apple",	200,	38],
		["kiwi",	130,	40],
		["orange",	90,		20],
		["grape",	380,	30],
		["peach",	400,	10],
		["cherry",	300,	5],
		["banana",	80,		36],
		["lemon",	150,	20] ]
total = [0, 0]
for i in range(0, len(items)):
	print(items[i][0].ljust(8)+" "+"{0:4d}".format(items[i][1])+" "+"{0:4d}".format(items[i][2])+" "+"{0:5d}".format(items[i][1] * items[i][2]))
	total[0] += items[i][2]
	total[1] += items[i][1] * items[i][2]
print("total".ljust(8)+" "+" "*4+" "+"{0:4d}".format(total[0])+" "+"{0:5d}".format(total[1]))