# 백준 9095 1,2,3더하기

num=int(input())
lt=[]

for i in range(num):
    lt.append(int(input()))

count=0
result=0
def foo(num,target):
    global count

    for i in range(1,4):
        if num+i<target:
            foo(num+i,target)
        elif num+i==target:
            count+=1

    
for i in range(len(lt)):
    target=lt[i]
    if target==1:
        print(1)
    elif target==2:
        print(2)
    elif target==3:
        print(4)
    elif target==0:
        print(0)
    else:
        foo(1,target)
        foo(2,target)
        foo(3,target)
        print(count)
        count=0