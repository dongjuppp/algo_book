# 백준 2798 블랙잭
from itertools import combinations

n,m=map(int,input().split( ))

lt=list(map(int,input().split( )))

combi=list(combinations(lt,3))

result=0
for i in range(len(combi)):
    s=sum(combi[i])

    if result<s and s<=m:
        result=s

print(result)