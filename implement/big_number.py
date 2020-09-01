# 프로그래머스 큰 수 만들기
from itertools import combinations
#4177252841
number = input()
k = int(input())

def find_big_index(lt,k,start):
    result=0
    #print(start,k)
    if k-start<2:
        if lt[start]>=lt[k]:
            return start
        else:
            return k
    
    for i in range(start,start+k+1):
        if lt[result]<lt[i]:
            result=i
    #print(result)
    return result

answer=''
answer_list=[]
lt = [(i) for i in number]
start=0
while(k>0):
    now=find_big_index(lt,k,start)
    print(now)
    answer_list.append((lt[now]))
    k=k-now
    start=now+1
    
    
#answer_list+=lt
answer=answer.join(answer_list)
print(str(answer))


