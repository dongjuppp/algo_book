# 책 314 만들 수 없는 금액
from itertools import combinations
num=int(input())

moneys=list(map(int,input().split( )))

combi=[]

for i in range(1,num+1):
    combi.append(list(combinations(moneys,i)))

money_list=[]

for i in range(len(combi)):
    for j in range(len(combi[i])):
        money_list.append(sum(combi[i][j]))

for i in range(1,sum(moneys)+1):
    if not i in money_list:
        print(i)
        break

