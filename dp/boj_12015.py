# 백준 12015 가장 긴 증가하는 부분 수열2
# dp + 이진탐색
import sys
import bisect

n=int(sys.stdin.readline())

lt=list(map(int,sys.stdin.readline().split()))
dp=[lt[0]]

for i in range(1,len(lt)):
    if dp[-1]<lt[i]:
        dp.append(lt[i])
    else:
        tmp=bisect.bisect_left(dp,lt[i])
        dp[tmp]=lt[i]

print(len(dp))