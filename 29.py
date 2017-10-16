#usr/bin/env python3

import sys

print("29. キャメル・ケース")

args = sys.argv
s = ""
for i in range(1,len(args)):
	s += args[i].capitalize()
print(s)