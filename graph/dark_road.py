# 어두운 길 책 397

house,light=map(int,input().split( ))

#city=[[] for i in range(city+1)]
lt=[]
total=0
for i in range(light):
    a,b,c=map(int,input().split( ))
    lt.append((c,a,b)) # a->b: c
    total+=c

lt.sort()

parents=[i for i in range(house+1)]

def find_parent(parents,x):
    if parents[x]!=x:
        parents[x]=find_parent(parents,parents[x])
    return parents[x]

def union_parent(parents,a,b):
    pa=find_parent(parents,a)
    pb=find_parent(parents,b)

    if pa>pb:
        parentsp[pa]=pb
    else:
        parents[pb]=pa

result=0
for i in range(len(lt)):
    if find_parent(parents,lt[i][1]) != find_parent(parents,lt[i][2]):
        union_parent(parents,lt[i][1],lt[i][2])
        result+=lt[i][0]
print(total-result)