file = open('day 3/input.txt','r')
lines = file.readlines()
file.close()

import re

pattern = re.compile(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)')

matches = []
for line in lines:
    match = pattern.findall(line)
    matches.extend(match)

total = 0

for match in matches:
    num1, num2 = map(int, match)
    total += num1 * num2

print(f"Total: {total}")

