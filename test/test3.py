from collections import deque
def solution(s):
    answer=1
    stck=[]

    stck.append(s[0])
    idx=1
    while idx<len(s):
        now=s[idx]
        if len(stck)==0 and idx<len(s):
            stck.append(now)
            idx+=1
            continue
        ex=stck.pop()

        if now!=ex:
            stck.append(ex)
            stck.append(now)
        idx+=1
        #print(stck)
    if len(stck)!=0:
        answer=0
    else:
        answer=1
        
    return answer

print(solution('baabaa'))
#print(solution('cbcb'))