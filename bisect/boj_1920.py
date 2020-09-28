# 백준 1920 수찾기

num1=int(input())

numbers=list(map(int,input().split( )))
numbers.sort()

target_num=int(input())

targets=list(map(int,input().split()))

result=[0]*target_num


def bisect(num,index):
    start=0
    end=num1-1
    global result

    while(start<=end):
        mid=(start+end)//2
        if num==numbers[mid]:
            result[index]=1
            break
        
        elif num>numbers[mid]:
            start=mid+1
        else:
            end=mid-1

for i in range(target_num):
    bisect(targets[i],i)

for i in range(len(result)):
    print(result[i])