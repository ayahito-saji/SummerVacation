#usr/bin/env python3

print("2.FizzBuzz問題")
for i in range(1,100 + 1):
	s = str(i)
	if i%3 == 0:
		s += "Fizz"
	if i%5 == 0:
		s += "Buzz"
	print(s)