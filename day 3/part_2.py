file = open('D:/(arguably) projects/advent-of-code/day 3/input.txt','r')
lines = file.readlines()
file.close()

import re

text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

mul_pattern = re.compile(r'mul\(\s*(\d+)\s*,\s*(\d+)\s*\)')

do_pattern = re.compile(r"do\(\)")
dont_pattern = re.compile(r"don't\(\)")

total = 0
mul_enabled = True

for text in lines:
    # Process the text
    i = 0
    while i < len(text):
        if text[i:i+4] == "do()":
            mul_enabled = True
            i += 4
            continue
        elif text[i:i+7] == "don't()":
            mul_enabled = False
            i += 7
            continue

        mul_match = mul_pattern.match(text, i)
        if mul_match and mul_enabled:
            num1, num2 = map(int, mul_match.groups())
            total += num1 * num2
            i += mul_match.end() - mul_match.start()
        else:
            i += 1

print(f"Total: {total}")

