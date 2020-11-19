# 책 368 고정점 찾기

num=int(input())

lt=list(map(int,input().split( )))
result=-1
def bisect():
    global result
    a=0
    b=len(lt)-1

    while a<=b:
        mid=(a+b)//2

        if lt[mid]==mid:
            result=mid
        
        if lt[mid]<mid:
            a=mid+1
        else:
            b=mid-1

bisect()
print(result)
