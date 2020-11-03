# 책 327 뱀

n=int(input())
k=int(input())

world=[[]]

for i in range(n):
    world.append([0 for i in range(n+1)])

for i in range(k):
    a,b=map(int,input().split( ))
    world[a][b]=1

world[1][1]=2

move=int(input())
turn=[]
time=[]
#상하좌우
x_move=[0,0,-1,1]
y_move=[-1,1,0,0]
for i in range(move):
    a,b=map(str,input().split( ))
    time.append(int(a))
    turn.append(b)

now=[1,1]
count=0
head_point_time=time.pop(0)

# 상하좌우 0,1,2,3
head_point=3
go1=0
go2=1
tail=[]
while True:  
    count+=1
    tail.append([now[0],now[1]])

    now[0]+=go1
    now[1]+=go2

    
    #벽꿍
    if now[0]>n or now[0]<1 or now[1]>n or now[1]<1:
        break
    #몸꿍
    col=0
    for i in tail:
        if now[0]==i[0] and now[1]==i[1]:
            col=1
            break

    if col==1:
        break

    if not(now[0]>n or now[0]<1 or now[1]>n or now[1]<1):
        if world[now[0]][now[1]]!=1:
            tail.pop(0)
        else:
            world[now[0]][now[1]]=0
    

    #뱡향 바꾸기
    if count==head_point_time:
        if len(turn)>0:
            t=turn.pop(0)
        if t=='D':
            if head_point==3:
                    head_point=1
            elif head_point==2:
                head_point=0
            elif head_point==1:
                head_point=2
            else:
                head_point=3
        if t=='L':
            if head_point==3:
                head_point=0
            elif head_point==2:
                head_point=1
            elif head_point==1:
                head_point=3
            else:
                head_point=2
        if len(time)>0:
            head_point_time=time.pop(0)

    #0123 상하좌우
    if head_point==0:
        go1=-1 #0
        go2=0
    elif head_point==1:
        go1=1
        go2=0
    elif head_point==2:
        go2=-1
        go1=0
    else:
        go2=1
        go1=0
    
        

print(count)


