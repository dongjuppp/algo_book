#백준 7576 토마토
from collections import deque
col,row=map(int,input().split( ))

world=[]
result=0

x_move=[0,0,-1,1]
y_move=[-1,1,0,0]

for i in range(row):
    world.append(list(map(int,input().split( ))))

q=deque()
for i in range(row):
    for j in range(col):
        if world[i][j]==1:
            q.append([i,j,0])


while q:
    now=q.popleft()

    for i in range(4):
        x=now[1]+x_move[i]
        y=now[0]+y_move[i]

        if x>=0 and x<col and y>=0 and y<row and world[y][x]==0:
            q.append([y,x,now[2]+1])
            if result<now[2]+1:
                result=now[2]+1
            world[y][x]=2

sign=0
for i in range(row):
    for j in range(col):
        if world[i][j]==0:
            sign=1
            break
if sign==0:
    print(result)
else:
    print(-1)