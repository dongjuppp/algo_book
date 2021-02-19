from math import gcd
def solution(n, m):
    answer = []
    a=gcd(n,m) # 최대공약수
    b=n*m//a # 최소공배수

    answer.append(a)
    answer.append(b)
    return answer

print(solution(2,5))


