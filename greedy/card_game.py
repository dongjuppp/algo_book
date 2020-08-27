# 책 96페이지
import sys

a,b = map(int,input().split())
result=0
for i in range(a):
    tmp=list(map(int,input().split()))
    min_value = min(tmp)
    result=max(result,min_value)

print(result)

