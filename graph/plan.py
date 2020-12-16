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

city,plan=map(int,input().split( ))

parents=[i for i in range(city+1)]

for i in range(1,city+1):
    lt=list(map(int,input().split( )))

    for j in range(len(lt)):
        if lt[j]==1:
            union_parents(parents,i,j)

course=list(map(int,input().split( )))

sign=0
ex=parents[course[0]]
for i in range(1,len(course)):
    if ex!=parents[course[i]]:
        sign=1
print(parents)
if sign==1:
    print('NO')
else:
    print('YES')
    
