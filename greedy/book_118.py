n,m=map(int,input().split( ))
a,b,d=map(int,input().split( ))

lt=[]
for i in range(n):
    lt.append(list(map(int,input().split())))

character_rotate_x=[-1,0,1,0]
character_rotate_y=[0,1,0,-1]

result=1
ex_move=0
while True:
    
    sign=0
    for i in range(4):
        x_move=a+character_rotate_x[i]
        y_move=b+character_rotate_y[i]

        if x_move>=0 and x_move<m and y_move>=0 and y_move<n:
            if lt[y_move][x_move]==0:
                result+=1
                a=x_move
                b=y_move
                lt[b][a]=2
                ex_move=i
                sign=1
    if sign==0:
        if lt[a-1][b]==1:
            break
        else:
            b=b+y_move[ex_move]*-1
            a=a+x_move[ex_move]*-1
            if not (a>=0 and a<m and b>=0 and b<n):
                break


print(result)