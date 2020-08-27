a = int(input())

lt = list(map(int,input().split()))

lt.sort()

result=0
tmp=0
for i in lt:
    tmp+=i
    result+=tmp

print(result)
