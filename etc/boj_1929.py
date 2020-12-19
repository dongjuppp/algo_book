# 백준 1929 소수 구하기

n,m=map(int,input().split( ))
lt=[i for i in range(m+1)]

def chae(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
        if count>2:
            return False
    return True

mid=int(m**0.5)


for number in range(2,mid+1):
    if lt[number]!=0:
        if chae(number):
            start=2
            while True:
                if number*start>len(lt)-1:
                    break
                
                lt[number*start]=0
                start+=1
            

for i in range(n,m+1):
    if lt[i]>1:
        print(lt[i])
        
