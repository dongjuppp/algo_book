# 백준 2468 안전지역
from collections import deque

n=int(input())

world=[]

x_move=[0,0,-1,1]
y_move=[-1,1,0,0]

small=101
big=0

for i in range(n):
    tmp=list(map(int,input().split( )))
    world.append(tmp)

    small=min(small,min(tmp))
    big=max(big,max(tmp))

def bfs(x,y,depth,visited):
    que=deque()
    que.append([x,y])

    while que:
        tmp=que.popleft()
        for i in range(4):
            now_x=tmp[0]+x_move[i]
            now_y=tmp[1]+y_move[i]

            if now_x>=0 and now_x<n and now_y>=0 and now_y<n and visited[now_y][now_x]==False and world[now_y][now_x]>depth:
                que.append([now_x,now_y])
                visited[now_y][now_x]=True


result=0
for i in range(0,big+1):
    visited=[[False]*n for _ in range(n)]
    tmp_result=0
    for j in range(n):
        for k in range(n):
            if visited[j][k]==False and world[j][k]>i:
                tmp_result+=1
                bfs(k,j,i,visited)
   
    if tmp_result>result:
        result=tmp_result

print(result)
    