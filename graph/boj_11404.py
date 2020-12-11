# 백준 11404 플로이드
INF=int(1e9)
num=int(input())

bus=int(input())

world=[]

for i in range(num+1):
    world.append([INF]*(num+1))

for i in range(1,num+1):
    for j in range(1,num+1):
        if i==j:
            world[i][j]=0

for i in range(bus):
    a,b,c=map(int,input().split( ))
    if world[a][b]==INF:
        world[a][b]=c
    else:
        if world[a][b]>c:
            world[a][b]=c

for k in range(1,num+1):
    for a in range(1,num+1):
        for b in range(1,num+1):
            world[a][b]=min(world[a][b],world[a][k]+world[k][b])

for i in range(1,num+1):
    for j in range(1,num+1):
        if world[i][j]>=INF:
            print(0,end=' ')
        else:
            print(world[i][j],end=' ')
    print()