# 화성탐사 책 388
import heapq

INF=int(1e9)
n=int(input())

world=[]
distance=[]
for i in range(n):
    world.append(list(map(int,input().split( ))))
    distance.append([INF]*n)
x_move=[0,0,-1,1]
y_move=[-1,1,0,0]

distance[0][0]=world[0][0]
def dik():
    q=[]
    heapq.heappush(q,(world[0][0],(0,0)))

    while q:
        dist,now=heapq.heappop(q)

        if dist>distance[now[0]][now[1]]:
            continue

        for i in range(4):
            now_x=now[1]+x_move[i]
            now_y=now[0]+y_move[i]

            if now_x<n and now_x>=0 and now_y<n and now_y>=0:
                cost=dist+world[now_y][now_x]

                if cost<distance[now_y][now_x]:
                    distance[now_y][now_x]=cost
                    heapq.heappush(q,(cost,(now_y,now_x)))

dik()
print(distance[n-1][n-1])
