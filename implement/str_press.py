# 책 323 문자열 압축


def get_same_len(s,s_size):
    result=(len(s)%s_size)
    prev=s[0:s_size]
    tmp=s_size
    now_s=s[0:len(s)-(len(s)%s_size)]
    count=0

    for i in range(tmp,len(now_s),s_size):
        if prev==now_s[i:i+s_size]:
            count+=1
            if i+s_size==len(now_s):
                result+=s_size+1
        else:
            if count>0:
                result+=s_size+1
            else:
                result+=s_size
            if i+s_size==len(now_s):
                result+=s_size
            prev=now_s[i:i+s_size]
            count=0
    
    
    return result


def solution2(s):
    answer = len(s)
    if answer==1:
        return 1
    for i in range(1,len(s)//2+1):
        tmp=get_same_len(s,i)
        if tmp<answer:
            answer=tmp
    return answer

def solution(s):
    answer=len(s)
    for step in range(1,len(s)//2+1):
        compressed=''
        prev=s[0:step]
        count=1

        for j in range(step,len(s),step):
            if prev==s[j:j+step]:
                count+=1
            else:
                compressed+=str(count)+prev if count >=2 else prev
                prev=s[j:j+step]
                count=1
        compressed+=str(count)+prev if count >=2 else prev
        answer=min(answer,len(compressed))
    return answer

print(solution('abcabcdede'))
print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))

print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
print(solution('b'))
print(solution('aaabaaab'))
print(solution('abcdabc'))

