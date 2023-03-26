# C - Socks
item_num = int(input().rstrip())
colors = sorted(input().rstrip().split(" "))

pair_num = 0
counter = 0

while counter < item_num - 1:
    if colors[counter] == colors[counter+1]:
        counter += 2
        pair_num += 1
    else:
        counter += 1

print(pair_num)
