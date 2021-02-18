row,col=map(int,input().split( ))

lt=[list(map(int,input())) for i in range(row)]

visited=[[False]*col for i in range(row)]

x_move=[0,0,-1,1]
y_move=[-1,1,0,0]

def dfs(r,c):

    for i in range(4):
        x=x_move[i]+c
        y=y_move[i]+r

        if y>=0 and y<row and x>=0 and x<col:
            if lt[y][x]==0 and not visited[y][x]:
                visited[y][x]=True
                dfs(y,x)

count=0
for i in range(row):
    for j in range(col):
        if lt[i][j]==0 and  not visited[i][j]:
            count+=1
            dfs(i,j)

print(count)
