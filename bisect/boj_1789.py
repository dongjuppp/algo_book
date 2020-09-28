# 백준 1789 수들의 합


num=int(input())


lt=[int((i*(i+1))/2) for i in range(93000)]

start=0
end=93000
result=0
while(start<=end):
    mid=(start+end)//2

    if lt[mid]<=num:
        result=mid
        start=mid+1
    else:
        end=mid-1

print(result)

