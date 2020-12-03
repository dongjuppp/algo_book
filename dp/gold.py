case=int(input())

n,m=map(int,input().split( ))

lt=list(map(int,input().split( )))

world=[]
index=0
for i in range(n):
    tmp=[]
    for j in range(m):
        tmp.append(lt[index+j])
    index+=m
    world.append(tmp)

dp=[]

for i in range(n):
    dp.append(world[i][0])

for i in range(1,m):
    tmp_dp=[0]*n
    for j in range(n):
        value=world[j][i]+dp[j]
        # j,j+1,j-1    i-1

        if j+1<n:
            value=max(value,world[j][i]+dp[j+1])
        if j-1>=0:
            value=max(value,world[j][i]+dp[j-1])
        tmp_dp[j]=value
    dp=tmp_dp

print(dp)
print(max(dp))