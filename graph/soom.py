# 숨바꼭질 책 390
import heapq

INF=int(1e9)
n,m=map(int,input().split( ))

world=[]
distance=[INF]*(n+1)
for i in range(n+1):
    world.append([])

for i in range(m):
    a,b=map(int,input().split( ))
    world[a].append(b)
    world[b].append(a)

def dik():
    global distance
    q=[]
    heapq.heappush(q,(0,1))

    while q:
        dist,now=heapq.heappop(q)

        if dist>distance[now]:
            continue

        for i in world[now]:
            cost=dist+1

            if cost<distance[i] and i!=1:
                distance[i]=cost
                heapq.heappush(q,(cost,i))
dik()
print(distance)