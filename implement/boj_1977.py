m = int(input())
n = int(input())

bottom = int(m**(1/2))
top = int(n**(1/2))


lt = []

for i in range(bottom, top + 1):
    multi = i**2
    if multi >= m and multi <= n:
        lt.append(i**2)

if len(lt) == 0:
    print('-1')
else:
    print(sum(lt))
    print(lt[0])