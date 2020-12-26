# 백준 18352 특정 거리의 도시 찾기
import heapq
INF=int(1e9)
city,road,k,x=map(int,input().split( ))

world=[[] for i in range(city+1)]

distance=[INF]*(city+1)

for _ in range(road):
    a,b=map(int,input().split( ))
    world[a].append(b)

q=[]

heapq.heappush(q,(0,x))
distance[x]=0
while q:
    dist,now=heapq.heappop(q)

    if dist>distance[now]:
        continue

    for i in range(len(world[now])):
        a=world[now][i]
        cost=dist+1
        if cost<distance[a]:
            distance[a]=cost
            heapq.heappush(q,(cost,a))

tmp=[]
for i in range(len(distance)):
    if distance[i]==k:
        tmp.append(i)
if len(tmp)==0:
    print(-1)
else:
    for i in range(len(tmp)):
        print(tmp[i])
