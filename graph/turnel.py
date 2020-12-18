# 행성 터널 책 398

num=int(input())

world=[]

for i in range(num):
    a,b,c=map(int,input().split( ))
    world.append([a,b,c])

def compute_length(a,b):
    return min(abs(a[0]-b[0]),abs(a[1]-b[1]),abs(a[2]-b[2]))
lt=[]

for i in range(len(world)):
    for j in range(len(world)):
        if i!=j:
            lt.append((compute_length(world[i],world[j]),i,j))
lt.sort()

parents=[i for i in range(num+1)]

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
result=0
for i in range(len(lt)):
    if find_parents(parents,lt[i][1])!=find_parents(parents,lt[i][2]):
        union_parents(parents,lt[i][1],lt[i][2])
        result+=lt[i][0]

print(result)