# 정확한 순위 책 386
INF=int(1e9)
students,rank=map(int,input().split( ))
graph=[]

for i in range(students+1):
    graph.append([INF]*(students+1))

for _ in range(rank):
    a,b=map(int,input().split( ))
    graph[a][b]=1
    

for i in range(students):
    for j in range(students):
        if i==j:
            graph[i][j]=0

for k in range(1,students):
    for a in range(1,students):
        for b in range(1,students):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])


count=0
for i in range(1,students+1):
    tmp=0
    for j in range(1,students+1):
        if graph[i][j]!=INF or graph[j][i]!=INF:
            tmp+=1
    if tmp==students-1:
        count+=1
print(count)