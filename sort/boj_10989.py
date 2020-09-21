# 백준 10989 실패

num=int(input())
lt=[0]*10005

for i in range(num):
    lt[int(input())]+=1


for i in range(len(lt)):
    for j in range(lt[i]):
        print(i)

