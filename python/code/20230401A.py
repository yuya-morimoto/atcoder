# A - Alternately
import sys

input = sys.stdin.readline

n = input().rstrip()
s = input().rstrip()

check_list = ["MM", "FF"]

if n == 1:
    print("Yes")
else:
    for check in check_list:
        if check in s:
            print("No")
            break
    else:
        print("Yes")
