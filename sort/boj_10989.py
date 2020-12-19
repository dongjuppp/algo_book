# 백준 10989 실패
import sys
num=int(input())
lt=[0]*10001

for i in range(num):
    lt[int(sys.stdin.readline().rstrip())]+=1


for i in range(len(lt)):
    for j in range(lt[i]):
        print(i)
