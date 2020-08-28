n = int(input())

lt=[]

for i in range(n):
    lt.append(int(input()))

lt.sort(reverse=True)

for i in range(n):
    lt[i]=lt[i]*(i+1)


print(max(lt))