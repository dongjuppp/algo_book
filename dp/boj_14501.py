# 백준 14501번 퇴사

n=int(input())
schedule=[]
for i in range(n):
    a,b=map(int,input().split( ))
    schedule.append([a,b])

cost=[0]*n

if not schedule[0][0]>n:
    cost[0]=schedule[0][1]

for i in range(1,n):
    if schedule[i][0]+(i)>n:
        cost[i]=0
        continue
    else:
        cost[i]=schedule[i][1]
    for j in range(i-1,-1,-1):
        if schedule[j][0]+j<=i:
            cost[i]=max(cost[i],schedule[i][1]+cost[j])
print(max(cost))
