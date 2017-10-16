#usr/bin/env python3

print("10. 素因数分解")
num = int(input("整数を入力してください"))

n = num
s = []
while n > 1:
	for k in range(2, n+1):
		if n % k == 0:
			s.append(k);
			n = int(n/k)
			break
print(str(num)+"の素因数分解の結果は"+str(s)+"です")