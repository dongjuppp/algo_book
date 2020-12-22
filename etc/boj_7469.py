# 백준 7469 현정이

length,case=map(int,input().split())

lt=list(map(int,input().split( )))

cases=[]

for _ in range(case):
    cases.append(list(map(int,input().split( ))))

result=[]

for i in range(case):
    now=cases[i]
    tmp_lt=lt[now[0]-1:now[1]]
    tmp_lt.sort()
    result.append(tmp_lt[now[2]-1])

for i in range(case):
    print(result[i])