#책 99페이지

target,num = map(int,input().split())

count=0

while(target>1):
    if target%num==0:
        target/=num
    else:
        target-=1
    count+=1

print(count)