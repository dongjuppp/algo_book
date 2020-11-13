# 백준 14502 연구소
from collections import deque
import copy

n,m=map(int,input().split())
world=[]

for i in range(n):
    tmp=list(map(int,input().split()))
    world.append(tmp)

#상하좌우
x_move=[0,0,-1,1]
y_move=[-1,1,0,0]

twos=[]

for i in range(n):
    for j in range(m):
        if world[i][j]==2:
            twos.append([i,j])

def check(tmp_world):
    result=0
    for i in range(n):
        for j in range(m):
            if tmp_world[i][j]==0:
                result+=1
    return result



def go(tmp_world):
    tmp=copy.deepcopy(tmp_world)
    #tmp=tmp_world[:]
    que=deque()
    for two in twos:
        que.append(two)
    
    while que:
        now=que.popleft()

        for i in range(4):
            x=now[1]+x_move[i]
            y=now[0]+y_move[i]

            if not(x<0 or x>=m or y<0 or y>=n ) and tmp[y][x]==0:
                tmp[y][x]=2
                que.append([y,x])
    return check(tmp)

def print_world(world):
    for i in range(n):
        print(world[i])


def compute():
    result=0
    #tmp_world=world[:]
    tmp_world=copy.deepcopy(world)

    for i in range(n):
        for j in range(m):
            for k in range(n):
                for q in range(m):
                    if i!=k or j !=q:
                        for r in range(n):
                            for t in range(m):
                                if (k!=r or q != t) and (i!=r or j!=t) and tmp_world[i][j]==0 and tmp_world[k][q]==0 and tmp_world[r][t]==0:
                                    tmp_world[i][j]=1
                                    tmp_world[k][q]=1
                                    tmp_world[r][t]=1
                                    
                                    tmp=go(tmp_world)
                                    if tmp>result:
                                        result=tmp
                                    tmp_world[i][j]=0
                                    tmp_world[k][q]=0
                                    tmp_world[r][t]=0
    return result

print(compute())




