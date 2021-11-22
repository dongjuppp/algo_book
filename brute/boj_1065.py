num = int(input())


def seperate_num(number):
    lt = []
    
    n = 10
    tmp = number
    while tmp>0:
        lt.append(tmp%n)
        tmp=tmp//n
    lt.reverse()
    return lt

def is_hansu(num_lt):
    if len(num_lt) == 1:
        return True
    
    gap = num_lt[0] - num_lt[1]
    
    for j in range(1, len(num_lt) - 1):
        if not (num_lt[j] - num_lt[j+1] == gap):
            return False
    return True
            

result = 0
for i in range(1, num + 1):
    l = seperate_num(i)
    
    if is_hansu(l):
        result+=1
    

print(result)