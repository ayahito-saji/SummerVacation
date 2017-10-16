#usr/bin/env python3

print("32. 文字列マッチ")

file_opener = open("constitution.txt",'r')

for line_data in file_opener:
	line_data = line_data.strip()
	if line_data.find("Constitusion"):
		print(line_data)