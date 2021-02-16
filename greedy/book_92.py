n,m,k=map(int,input().split( ))

lt=list(map(int,input().split( )))
lt.sort(reverse=True)
result=0
for i in range(1,m+1):
    if(i%k==0):
        result+=lt[1]
    else:
        result+=lt[0]

print(result)