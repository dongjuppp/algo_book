word = list(input())
dp = [0 for i in range(len(word)+1)]
target = input()
target_len = len(target)

def is_same(a, b):
    for i in range(len(b)):
        if a[i] != b[i]:
            return False
    return True

if len(word) < target_len:
    print('0')
else:
    if is_same(word[0:target_len], target):
        dp[target_len]=1

    for i in range(1, len(word)-target_len+1):
        if is_same(word[i:i+target_len], target):
            big = 0
            for j in range(i, 0, -1):
                if dp[j] > big:
                    big = dp[j]
            dp[i+target_len] = big + 1

    print(max(dp))
