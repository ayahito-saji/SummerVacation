#usr/bin/env python3

print("31. 行数")

file_opener = open("constitution.txt",'r')

count = 0
for line_data in file_opener:
	count += 1
print(count)