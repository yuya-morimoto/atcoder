# C - Gap Existence
import sys

input = sys.stdin.readline

n, x = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))

if x == 0:
    print("Yes")
    exit()

hash_table = {}
for i in range(n):
    hash_table[a[i] - x] = True

for i in range(n):
    if a[i] in hash_table:
        print("Yes")
        exit()

print('No')
