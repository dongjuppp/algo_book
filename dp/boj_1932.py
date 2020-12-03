# 백준 1932번 정수 삼각형

n=int(input())

world=[]
for i in range(n):
    world.append(list(map(int,input().split( ))))

for i in range(1,n):
    for j in range(len(world[i])):
        if j+1==len(world[i]):
            world[i][j]=world[i][j]+world[i-1][j-1]
        else:
            if j-1>=0:
                world[i][j]=max(world[i][j]+world[i-1][j],world[i][j]+world[i-1][j-1])
            else:
                world[i][j]=world[i][j]+world[i-1][j]
print(max(world[n-1]))