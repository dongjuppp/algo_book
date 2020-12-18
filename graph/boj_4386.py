# 백준 4386 별자리

def compute(a,b):
    x=abs(a[0]-b[0])
    y=abs(a[1]-b[1])
    return (x**2+y**2)**0.5

def find_parents(parents,x):
    if parents[x]!=x:
        parents[x]=find_parents(parents,parents[x])
    return parents[x]

def union_parents(parents,a,b):
    pa=find_parents(parents,a)
    pb=find_parents(parents,b)

    if pa>pb:
        parents[pa]=pb
    else:
        parents[pb]=pa
    
n=int(input())



world=[]

for i in range(n):
    world.append(list(map(float,input().split( ))))

graph=[]
parents=[i for i in range(n+1)]
for i in range(n):
    for j in range(n):
        if i!=j:
            graph.append((compute(world[i],world[j]),i,j))
graph.sort()
result=0
for i in range(len(graph)):
    if find_parents(parents,graph[i][1]) != find_parents(parents,graph[i][2]):
        union_parents(parents,graph[i][1],graph[i][2])
        result+=graph[i][0]
print("%.2f" % (result))