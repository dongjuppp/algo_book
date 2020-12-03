# 백준 18353번 병사 배치하기

n=int(input())

lt=list(map(int,input().split( )))

dp=[1]*n

for i in range(1,n):
    for j in range(i,-1,-1):
        if lt[i]<lt[j-1] and j-1>=0:
            dp[i]=max(dp[i],dp[j-1]+1)


print(n-max(dp))