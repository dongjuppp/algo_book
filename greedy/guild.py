# 책 311 모험가 길드

num=int(input())

lt=list(map(int,input().split( )))

lt.sort()

result=0

count=0

for i in range(len(lt)):
    count+=1

    if lt[i]==count:
        result+=1
        count=0

print(result)
