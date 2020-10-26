# 백준 1647 도시 분할 계획

home,road=map(int,input().split( ))

graph=[]
parents=[i for i in range(home+1)]

for i in range(road):
    a,b,c=map(int,input().split( ))
    graph.append((c,a,b))


def find_parents(parents,x):
    if parents[x]!=x:
        parents[x]=find_parents(parents,parents[x])
    return parents[x]

def union_parents(parents,a,b):
    a=find_parents(parents,a)
    b=find_parents(parents,b)

    if a>b:
        parents[a]=b
    else:
        parents[b]=a

graph.sort()
result=0
minus=0
for i in range(0,len(graph)):
    if find_parents(parents,graph[i][1]) != find_parents(parents,graph[i][2]):
        result+=graph[i][0]
        minus=graph[i][0]
        union_parents(parents,graph[i][1],graph[i][2])

print(result-minus)