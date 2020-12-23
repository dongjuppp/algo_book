# 백준 1541 괄호
import re

s=input()

numbers=re.split('[-,+]',s)
numbers=[int(i) for i in numbers]
lt2=re.split('[0 1 2 3 4 5 6 7 8 9]',s)
compute=[]
for i in range(len(lt2)):
    if lt2[i]=='-' or lt2[i]=='+':
        compute.append(lt2[i])



idx=0
minus=0
plus=numbers[0]

sign=1
for i in range(len(compute)):
    if compute[i]=='-':
        minus+=numbers[i+1]
        sign=0
    elif compute[i]=='+' and sign==1:
        plus+=numbers[i+1]
    elif compute[i]=='+' and sign==0:
        minus+=numbers[i+1]
    

print(plus-minus)
    