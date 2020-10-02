# 백준 11726 타일

num=int(input())

dp=[0]*1005

dp[1]=1
dp[2]=2

for i in range(3,num+1):
    dp[i]=(dp[i-1]+dp[i-2])%10007

print(dp[num])