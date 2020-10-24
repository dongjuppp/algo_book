# 백준 1916번 최소비용 구하기

import heapq

INF=int(1e9)

v=int(input())
e=int(input())

graph=[[] for i in range(v+1)]
distance=[INF]*(v+1)

for i in range(e):
    a,b,c=map(int,input().split( ))
    graph[a].append((b,c))

start,end=map(int,input( ).split( ))

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

            if distance[i[0]]>cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))


dik(start)

print(distance[end])