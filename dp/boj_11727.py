num=int(input())

dp=[1,3]

for i in range(2,num+1):
    dp.append(dp[i-1]+dp[i-2]*2)


print(dp[num-1]%10007)