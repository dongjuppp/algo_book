from math import sqrt
def solution(n):
    answer = 0
    num=sqrt(n)
    
    if num%1==0:
        answer=int((num+1)**2)
    else:
        answer=-1
    return answer

print(solution(121))