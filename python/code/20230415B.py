# A - Job Interview
import sys

input = sys.stdin.readline

n = int(input().rstrip())
a = [list(map(int, input().rstrip().split())) for _ in range(n)]
b = [list(map(int, input().rstrip().split())) for _ in range(n)]

def rotate(matrix):
    N = len(matrix)
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[N - j - 1][i]
            matrix[N - j - 1][i] = matrix[N - i - 1][N - j - 1]
            matrix[N - i - 1][N - j - 1] = matrix[j][N - i - 1]
            matrix[j][N - i - 1] = tmp

for _ in range(4):
    rotate(a)
    flag = False
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                if a[i][j] == b[i][j]:
                    flag = False
                else:
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    else:
        print("Yes")
        break
else:
    print("No")
