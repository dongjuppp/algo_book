# 책 220페이지 개미전사

num=int(input())

lt=list(map(int,input().split()))

dp=[lt[0],lt[1],lt[2]+lt[0]]

for i in range(3,len(lt)):
    dp.append(max(dp[i-2]+lt[i],dp[i-3]+lt[i]))

print(max(dp))
