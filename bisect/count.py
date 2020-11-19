# 책 367 정렬된 배열에서 특정 수의 개수 구하기

num,target=map(int,input().split())

lt=list(map(int,input().split( )))

visit=[False for i in range(num)]

a=0
b=len(visit)-1
start=0
def bisect():
    global a,b
    start=-1
    while a<=b:
        mid=(a+b)//2
        if lt[mid]==target:
            if mid==0:
                start=mid
            elif lt[mid-1]<target:
                start=mid
    
        if lt[mid]<target:
            a=mid+1
        else:
            b=mid-1
    count=0
    if start==-1:
        return -1
    for i in range(start,len(lt)):
        if lt[i]!=target:
            break
        count+=1
    return count

print(bisect())
