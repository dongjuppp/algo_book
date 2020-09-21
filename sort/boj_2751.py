#백준 2751

num=int(input())
lt=[0]*10000001
for i in range(num):
    lt[int(input())]+=1


for i in range(len(lt)):
    for j in range(lt[i]):
        print(i)