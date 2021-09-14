from itertools import combinations
a,target = list(map(int, input().split( )))

lt = list(map(int, input().split( )))

result = 0

for i in range(1,a+1):
    per = list(combinations(lt,i))
    for j in range(len(per)):
        num = sum(per[j])
        if num == target:
            result += 1

print(result)