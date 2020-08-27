# 책92페이지
import sys

n,m,k = map(int,sys.stdin.readline().rstrip().split())

n_list = list(map(int,sys.stdin.readline().rstrip().split()))

n_list.sort(reverse=True)

result=0
count=0

a=n_list[0]
b=n_list[1]

for i in range(m):
    if count<k:
        result+=a
        count+=1
    else:
        result+=b
        count=0
    
print(result)
