import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (N+1)
stacks = [-1000000001]
leng = 0

for i in range(1, N+1):
    if stacks[-1] < num[i]:
        stacks.append(num[i])
        dp[i] = len(stacks) - 1
        leng = dp[i]
    else:
        dp[i] = bisect_left(stacks, num[i]) 
        stacks[dp[i]] = num[i] 
print(leng) 

result = []
for i in range(N, 0, -1):
    if dp[i] == leng:
        result.append(num[i])
        leng -= 1
        
result.reverse()
print(*result)