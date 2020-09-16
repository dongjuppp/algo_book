# 백준 2178 미로 탐색

from collections import deque

#상하좌우
x_move=[0,0,-1,1]
y_move=[-1,1,0,0]

h,w=map(int,input().split( ))

graph=[]
visited=[]
result=99999999999999999999999999

for i in range(h):
    tmp=list(map(int,input()))
    graph.append(tmp)
    visited.append([False]*w)


def bfs(start_x,start_y,r):
    global result
    queue=deque()
    queue.append([start_x,start_y,r])
    visited[start_y][start_x]=True

    while queue:
        v=queue.popleft()

        if v[0]==w-1 and v[1]==h-1:
            result=min(result,v[2])
        
        for i in range(4):
            tmp_x=v[0]+x_move[i]
            tmp_y=v[1]+y_move[i]

            if tmp_x<0 or tmp_x>=w or tmp_y<0 or tmp_y>=h:
                continue
            elif graph[tmp_y][tmp_x]==0:
                continue
            
            if not visited[tmp_y][tmp_x]:
                queue.append([tmp_x,tmp_y,v[2]+1])
                visited[tmp_y][tmp_x]=True

bfs(0,0,1)
print(result)
