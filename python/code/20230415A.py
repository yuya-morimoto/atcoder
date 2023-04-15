# A - Job Interview
import sys

input = sys.stdin.readline

n = input().rstrip()
s = input().rstrip()

print("Yes" if "o" in s and not "x" in s else "No")