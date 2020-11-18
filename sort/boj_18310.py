# 백준 18310 안테나

num=int(input())

lt=list(map(int,input().split( )))
lt.sort()
mid=0
if num%2==0:
    mid=(num//2)-1
else:
    mid=num//2

print(lt[mid])