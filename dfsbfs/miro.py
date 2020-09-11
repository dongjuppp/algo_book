#책 152페이지 미로탈출
from collections import deque

n,m = map(int,input().split())

lt=[]
visit=[]
for i in range(n):
    lt.append(list(map(int,input())))
    visit.append([False]*m)

result=999999999999

#상하좌우
x_move=[0,0,-1,1]
y_move=[-1,1,0,0]

def bfs(x,y,r):
    global result
    queue = deque()
    queue.append([x,y,r])
    visit[y][x]=True

    while queue:
        v=queue.popleft()
        
        v[2]+=1
        if v[0]==m-1 and v[1]==n-1:
            result = min(result,v[2])
        

        for i in range(len(x_move)):
            tmp_x=v[0]+x_move[i]
            tmp_y=y+v[1]+y_move[i]

            if tmp_x<=-1 or tmp_x>=m or tmp_y<=-1 or tmp_y>=n or lt[tmp_y][tmp_x]==0 or visit[tmp_y][tmp_x]==True:
                continue
            if not visit[tmp_y][tmp_x]:
                queue.append([tmp_x,tmp_y,v[2]])
                visit[tmp_y][tmp_x]=True

bfs(0,0,0)
print(result)