#usr/bin/env python3

import math

print("9. 素数の一覧")
num = int(input("整数を入力してください"))

sieve = [True] * (num)
sieve[0] = False
for k in range(2, int(math.sqrt(num))+1):
	for i in range(2, int(num / k) + 1):
		sieve[k * i - 1] = False

for n in range(1, num + 1):
	if(sieve[n-1] == True):
		print(str(n)+", ", end="")