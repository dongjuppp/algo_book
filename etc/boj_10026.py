#백준 10026 적록색약
from collections import deque
n=int(input())

world=[]
x_move=[0,0,-1,1]
y_move=[-1,1,0,0]


for i in range(n):
    world.append(list(map(str,input())))

def bfs(sign): # sign=0=적록
    visited=[[False]*n for i in range(n)]
    
    result=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                q=deque()
                q.append([i,j])
                #now_color=world[i][j]
                result+=1
                while q:
                    now=q.popleft()
                    #visited[now[0]][now[1]]=True
                    now_color=world[now[0]][now[1]]
                    

                    for k in range(4):
                        x=now[1]+x_move[k]
                        y=now[0]+y_move[k]

                        
                        if x>=0 and x<n and y>=0 and y<n and visited[y][x]==False:
                            if sign==0:
                                if now_color=='B' and world[y][x]=='B':
                                    q.append([y,x])
                                    visited[y][x]=True
                                elif (now_color=='R' or now_color=='G') and (world[y][x]=='R' or world[y][x]=='G'):
                                    q.append([y,x])
                                    visited[y][x]=True
                            else:
                                if now_color==world[y][x]:
                                    q.append([y,x])
                                    visited[y][x]=True
                
    return result


b=bfs(0)                            
a=bfs(1)


print(str(a)+' '+str(b))