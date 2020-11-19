# 백준 2110 공유기 설치

num,c=map(int,input().split( ))

lt=[]

for i in range(num):
    lt.append(int(input()))

lt.sort()

l=lt[0]
r=lt[num-1]

def bisect():
    a=0
    b=num-1
    mid=(a+b)//2

    
        
    