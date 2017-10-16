#usr/bin/env python3

print("7. 最大公約数")
a = int(input("整数aを入力してください"))
b = int(input("整数bを入力してください"))

g = 0
for i in range(1, min(a, b) + 1):
	if a%i == 0 and b%i == 0:
		g = i
print("最大公約数は"+str(g)+"です")