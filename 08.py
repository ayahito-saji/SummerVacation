#usr/bin/env python3

import math

print("8. 素数判定")
num = int(input("整数を入力してください"))

isPrimeNumber = False
if num >= 2:
	isPrimeNumber = True
	for i in range(2, int(math.sqrt(num))+1):
		if num % i == 0:
			isPrimeNumber = False
			break
if isPrimeNumber:
	print(str(num)+"は素数です")
else:
	print(str(num)+"は素数ではありません("+str(i)+"の倍数)")