# B - Chessboard
import sys

input = sys.stdin.readline

eng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for row_num in range(8, 0, -1):
    row = input().rstrip()
    if '*' in row:
        print(f'{eng[row.index("*")]}{row_num}')
        break
