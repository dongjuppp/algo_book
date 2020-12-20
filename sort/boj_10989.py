# 백준 10989 실패
import sys
input=sys.stdin.readline

array_list=[0 for i in range(10000)]
num=int(input())

for cnt in range(num):
    array_list[int(input())-1]+=1
    

for cnt in range(0,10000):
    if array_list[cnt]!=0:
        for number in range(array_list[cnt]):
            print(cnt+1)
