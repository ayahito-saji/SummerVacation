#usr/bin/env python3

print("6. 階乗")
num = int(input("負でない整数を入力してください"))
fac = 1

if(num < 0):
	fac = -1
	print("負でない整数を入力してください")
if(num == 0):
	fac = 1
else:
	k = num
	while k > 1:
		fac *= k
		k -= 1
if fac !=-1:
	print(str(num)+"!の値は"+str(fac)+"です")