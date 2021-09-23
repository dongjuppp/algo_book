#백준 1339번 단어 수학
import operator

num = int(input())

nums = ['0','1','2','3','4','5','6','7','8','9']

lt = []

dicts = {}

for i in range(num):
    l = list(input())
    lt.append(l)
    for j in range(len(l)):
        dicts[l[j]] = 0

for i in range(num):
    now = lt[i]
    le = len(now)
    for j in range(le):
        dicts[now[j]] += 10 ** (le - j)

sdict = sorted(dicts.items(), key = operator.itemgetter(1), reverse = True)


for i in range(len(sdict)):
    n = sdict[i]
    dicts[n[0]] = nums.pop()


for i in range(len(lt)):
    for j in range(len(lt[i])):
        lt[i][j] = dicts[lt[i][j]]



result = 0
for i in range(len(lt)):
    n = int(''.join(lt[i]))
    result+=n

print(result)

