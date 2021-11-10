target = int(input())

lt = list(map(int, input().split(' ')))
card_len = len(lt)
dp = [0 for i in range(target + 1)]
dp[1] = lt[0]

for i in range(2, target + 1):
    for j in range(1, i + 1):
        if j > card_len:
            break
        dp[i] = max(dp[i - j] + lt[j-1], dp[i])


print(dp[target])