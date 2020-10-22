import heapq
INF = int(1e9)

company=0
road=0

company,road=map(int,input().split())

graph=[[] for i in range(company+1)]

distance=[INF]*(company+1)

for i in range(road):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

k,x=map(int,input().split( ))

def dik(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dik(1)

tmp=distance[x]
distance=[INF]*(company+1)

dik(x)
tmp+=distance[k]


print()
print(tmp)

