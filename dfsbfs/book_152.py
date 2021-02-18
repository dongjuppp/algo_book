from collections import deque

row,col=map(int,input().split( ))

lt=[list(map(int,input())) for i in range(row)]

result=int(10e9)

x_move=[0,0,-1,1]
y_move=[-1,1,0,0]
def bfs():
    global result
    que=deque()
    que.append([0,0,1]) # 좌표x,y,거리
    
    while que:
        now=que.popleft()
        
        if now[0]==col-1 and now[1]==row-1:
            print(now)
            result=min(result,now[2])
            break
        
        for i in range(4):
            x=x_move[i]+now[0]
            y=y_move[i]+now[1]

            if x>=0 and x<col and y>=0 and y<row:
                if lt[y][x]==1:
                    que.append([x,y,now[2]+1])

bfs()

print(lt)

