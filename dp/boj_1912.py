# 백준 1912 연속합

num=int(input())
lt=list(map(int,input().split( )))
dp=[0]*num
dp[0]=lt[0]


for i in range(1,num):
    dp[i]=max(dp[i-1]+lt[i],lt[i])

print(max(dp))