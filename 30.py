#usr/bin/env python3

import sys

print("30. スネーク・ケース")

args = sys.argv
s = ""
for i in range(1,len(args)):
	s += args[i].lower()+"_"
s = s[:-1]
print(s)