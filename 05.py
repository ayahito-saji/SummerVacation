#usr/bin/env python3

print("5. 総和")
num = int(input("数を入力してください"))
sum = 0
for i in range(1, num+1):
	sum += i
print("1から"+str(num)+"までの総和は"+str(sum)+"です")