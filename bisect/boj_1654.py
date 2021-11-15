k, n = map(int,input().split(' '))

lt = []

for _ in range(k):
    lt.append(int(input()))

lt = sorted(lt)


start = lt[k - 1]

a = 1
b = start 
result = 0
    
while (a<=b):
    mid = (a+b)//2
        
    tmp_lensum = 0
    for i in range(len(lt)):
        tmp_lensum+= lt[i] // mid
        
    if tmp_lensum >= n and result < mid:
        result = mid
        
    if tmp_lensum >= n :
        a = mid + 1
    else:
        b = mid - 1
    
print(result)