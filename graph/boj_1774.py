# 백준 1774 우주신과 교감

n,m=map(int,input().split( ))
result=0
world=[0]
parents=[i for i in range(n+1)]
for i in range(n):
    world.append(list(map(int,input().split( ))))

contect=[]
for i in range(m):
    contect.append(list(map(int,input().split( ))))

def compute(a,b):
    x=abs(a[0]-b[0])
    y=abs(a[1]-b[1])
    return (x**2+y**2)**0.5

def find_parent(parents,x):
    if parents[x]!=x:
        parents[x]=find_parent(parents,parents[x])
    return parents[x]

def union_parents(parents,a,b):
    pa=find_parent(parents,a)
    pb=find_parent(parents,b)

    if pa>pb:
        parents[pa]=pb
    else:
        parents[pb]=pa

for i in range(len(contect)):
    union_parents(parents,contect[i][0],contect[i][1])
    
graph=[]

for i in range(1,len(world)):
    for j in range(1,len(world)):
        if i!=j :
            graph.append((compute(world[i],world[j]),i,j))

graph.sort()

for i in range(len(graph)):
    if find_parent(parents,graph[i][1])!=find_parent(parents,graph[i][2]):
        union_parents(parents,graph[i][1],graph[i][2])
        result+=compute(world[graph[i][1]],world[graph[i][2]])
        

print("%.2f" % (result))
