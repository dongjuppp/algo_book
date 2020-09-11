#책 152페이지 미로탈출
from collections import deque

n,m = map(int,input().split())

lt=[]
visit=[]
for i in range(n):
    lt.append(list(map(int,input())))
    visit.append([False]*m)

result=999999999999
def bfs(x,y,r):
    if x<=-1 or x>=m or y<=-1 or y>=n:
        return
    if x+1==m and y+1==n:
        result=min(result,r)
        return
    if lt[y][x]==1:
        queue=deque()
        queue.append([x,y])
        visit[y][x]=True

    while queue:
        v=queue.popleft()
        bfs(v[0]-1,v[1],r+1)
        bfs(v[0]+1,v[1],r+1)
        bfs(v[0],v[1]+1,r+1)
        bfs(v[0],v[1]-1,r+1)

bfs(0,0,result)

print(result)




