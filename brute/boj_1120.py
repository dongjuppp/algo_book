a, b = map(str, input().split(' '))


result = 500

gap = len(b) - len(a)

for i in range(gap+1):
    tmp = '0'*i + a + '0'*(gap-i)
    
    count = 0
    for j in range(len(b)):
        
        if tmp[j] != b[j]:
            count += 1
    
    result = min(result, count)
        

print(result - gap)
    
    