from math import *

def compute(n):
    lt=[1,n]
    for i in range(2,floor(sqrt(n))+1):
        if n%i==0:
            lt.append(i)
            lt.append(n//i)
    return sum(lt)==n*2


for i in range(2,1000):
    if compute(i):
        print(i)