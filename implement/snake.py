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
tail=0
go1=0
go2=1
while True:  
    count+=1
    #벽꿍
    if now[0]+go1>n or now[0]+go1<1 or now[1]+go2>n or now[1]+go2<1:
        break
    #몸꿍
    col=0
    prev1=now[0]-go1
    prev2=now[1]-go2
    
    for i in range(tail):
        if i in time:
            pass
        if prev1==now[0] and prev2==now[0]:
            col=1

    if col==1:
        break

    if world[now[0]+go1][now[1]+go2]==1:
        tail+=1
        world[now[0]+go1][now[1]+go2]=0

    now[0]+=go1
    now[1]+=go2

    #뱡향 바꾸기
    for i in range(time):
        if count==i:
            t=turn[i]
            if t=='D':
                if head_point==3:
                    head_point=1
                elif head_point==2:
                    head_point=0
                elif head_point==1:
                    head_point=3
                else:
                    head_point=2
            if t=='L':
                if head_point==3:
                    head_point=0
                elif head_point==2:
                    head_point=1
                elif head_point==1:
                    head_point=2
                else:
                    head_point=3
            break

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


