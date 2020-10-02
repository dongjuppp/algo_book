# 책 223페이지 바닥 공사

num=int(input())

dp=[0]*1000
dp[1]=1
dp[2]=3

for i in range(3,num+1):
    dp[i]=(dp[i-1]+2*dp[i-2])%796796
print(dp[num])