# 책 315 볼링공 고르기

num,found=map(int,input().split( ))

lt=list(map(int,input().split( )))

total=(num*(num-1))//2
lt.sort()

dupl=[1 for i in range(max(lt)+1)]

start=lt[0]

for i in range(1,len(lt)):
    if start==lt[i]:
        dupl[lt[i]]+=1
    else:
        start=lt[i]

for du in dupl:
    if du>1:
        total-=(du*(du-1))//2
        print((du*(du-1))//2)


print(total)
