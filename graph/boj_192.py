# 백준 1922 네트워크 연결

computer=int(input())
net=int(input())

graph=[]
parents=[i for i in range(computer+1)]

for i in range(net):
    a,b,c=map(int,input().split( ))
    graph.append((c,a,b))

graph.sort()

def find_patents(parents,x):
    if parents[x]!=x:
        parents[x]=find_patents(parents,parents[x])
    return parents[x]

def union_parents(parents,a,b):
    a=find_patents(parents,a)
    b=find_patents(parents,b)

    if a>b:
        parents[a]=b
    else:
        parents[b]=a

result=0
for i in graph:
    if find_patents(parents,i[1])!=find_patents(parents,i[2]):
        result+=i[0]
        union_parents(parents,i[1],i[2])

print(result)