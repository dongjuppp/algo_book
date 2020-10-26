# 백준 2887 행성 터널

num=int(input( ))
stars=[]
graph=[]

for i in range(num):
    stars.append(list(map(int,input().split( ))))

    for j in range(0,len(stars)-1):
        cost=min(abs(stars[j][0]-stars[i][0]),abs(stars[j][1]-stars[i][1]),abs(stars[j][2]-stars[i][2]))
        graph.append((cost,i,j))

parents=[i for i in range(num+1)]


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
print(graph)
result=0
for i in graph:
    if find_parents(parents,i[1])!=find_parents(parents,i[2]):
        result+=i[0]
        union_parents(parents,i[1],i[2])

print(result)

