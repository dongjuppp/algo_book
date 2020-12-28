# 백준 2583 영역 구하기
from collections import deque
from sys import*
setrecursionlimit(10**6)

row,col,k = map(int,input().split( ))

world=[[0]*col for _ in range(row)]

for _ in range(k):
    x1,y1,x2,y2=map(int,input().split( ))

    for i in range(x1,x2):
        for j in range(y1,y2):
            world[j][i]=1

x_move=[0,0,-1,1]
y_move=[-1,1,0,0]
count=0
def dfs(x,y):
    global count,world
    world[y][x]=1
    #count+=1
    for i in range(4):
        now_x=x+x_move[i]
        now_y=y+y_move[i]

        if now_x>=0 and now_x<col and now_y>=0 and now_y<row and world[now_y][now_x]==0:
            
            count+=1
            dfs(now_x,now_y)


def bfs(x,y):
    global count
    que=deque()
    que.append([x,y])
    
    while que:
        now=que.popleft()
        count+=1
        for i in range(4):
            now_x=now[0]+x_move[i]
            now_y=now[1]+y_move[i]

            if now_x>=0 and now_x<col and now_y>=0 and now_y<row and world[now_y][now_x]==0:
                world[now_y][now_x]=1
                que.append([now_x,now_y])

result=[]
for i in range(row):
    for j in range(col):
        if world[i][j]==0:
            world[i][j]=0
            dfs(j,i)
            result.append(count)
            count=0

result.sort()
print(len(result))

for i in range(len(result)):
    print(result[i]+1,end=' ')
    