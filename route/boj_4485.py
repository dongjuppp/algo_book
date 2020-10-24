# 백준 젤다 4485

import heapq

INF=(1e9)

#상하좌우
x_move=[0,0,-1,1]
y_move=[1,-1,0,0]

result=99999999999

def dik(graph,size):
    global result
    distance=[]

    for i in range(size):
        distance.append([INF]*size)
    q=[]
    heapq.heappush(q,(graph[0][0],[0,0]))
    distance[0][0]=graph[0][0]

    while q:
        dist,now=heapq.heappop(q)

        if distance[now[0]][now[1]]<dist:
            continue

        for i in range(4):
            x_tmp=x_move[i]+now[1]
            y_tmp=y_move[i]+now[0]

            if x_tmp<=-1 or x_tmp>=size or y_tmp<=-1 or y_tmp>=size:
                continue
            cost=dist+graph[y_tmp][x_tmp]

            if cost<distance[y_tmp][x_tmp]:
                distance[y_tmp][x_tmp]=cost
                heapq.heappush(q,(cost,[y_tmp,x_tmp]))
    
    result=min(result,distance[size-1][size-1])




lt=[]
while True:
    x=int(input())
    
    if x==0:
        break

    graph=[]
    for i in range(x):
        graph.append(list(map(int,input().split( ))))
        
    dik(graph,x)
    lt.append(result)
    result=99999999999

for i in range(len(lt)):
    print('Problem '+str(i+1)+': '+str(lt[i]))