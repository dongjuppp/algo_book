from collections import deque

case=int(input())
#x,y
moves=[[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-1,2],[-2,1]]
result=[]
for _ in range(case):
    leng=int(input())
    world=[[0]*leng for i in range(leng)]
    x,y=map(int,input().split( ))
    a,b=map(int,input().split( ))

    que=deque()
    que.append([x,y,0])

    while que:
        now=que.popleft()
        if now[0]==a and now[1]==b:
            result.append(now[2])
            break


        for i in range(8):
            x=now[0]+moves[i][0]
            y=now[1]+moves[i][1]

            if x>=0 and x<leng and y>=0 and y<leng:
                if world[y][x]==0:
                    world[y][x]=1
                    que.append([x,y,now[2]+1])

for i in range(len(result)):
    print(result[i])