# A - Probably English


n = int(input())
w = list(input().split())

com = set(w) & set("and,not,that,the,you".split(','))

if len(com) > 0:
    print("Yes")
else:
    print("No")
