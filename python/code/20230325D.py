# D - Three Days Ago
from collections import Counter
import sys

input = sys.stdin.readline

text = input().rstrip()
bit = 0
counter = Counter()
counter[bit] += 1
for char in text:
    bit = bit ^ (1 << int(char))
    counter[bit] += 1

ans = 0

for value in counter.values():
    ans += value * (value - 1) // 2

print(ans)
