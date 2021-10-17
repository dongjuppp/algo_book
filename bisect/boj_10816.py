N = int(input())

lt = list(map(int, input().split()))
lt.sort()

M = int(input())

targets = list(map(int, input().split()))

my_dict = {}
for i in range(N):
    if lt[i] in my_dict:
        my_dict[lt[i]] += 1
    else:
        my_dict[lt[i]] = 1


for i in range(M):
    if targets[i] in my_dict:
        print(my_dict[targets[i]], end=' ')
    else:
        print(0, end=' ')