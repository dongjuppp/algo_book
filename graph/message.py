import heapq

INF=int(1e9)

city,road,start=map(int, input().split( ))

graph=[[] for i in range(city+1)]

distance=[INF]*(city+1)

for i in range(road):
    a,b,c=map(int,input().split( ))
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=i[1]+dist

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)
n=0
m=0
for i in range(1,city+1):
    if not distance[i]==INF:
        n+=1
        m+=distance[i]

print(str(n)+' '+str(m))
