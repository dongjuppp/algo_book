# 책 347 괄호 변환 프로그래머스 60058


def check_collection(string):
    lt=[]

    for char in string:
        if char=='(':
            lt.append('(')
        else:
            if len(lt)==0:
                return False
            lt.pop()
    if len(lt)==0:
        return True
    else:
        return False

def divide(string):
    result=['','']
    count=0
    for i in range(len(string)):
        if string[i]=='(':
            count+=1
        else:
            count+=-1
        if count==0:
            result[0]=string[:i+1]
            result[1]=string[i+1:]
            break
    
    return result

def reverse(string):
    result=''
    for i in range(1,len(string)-1):
        if string[i]=='(':
            result+=')'
        else:
            result+='('
    return result


def final(p):
    answer = ''
    if p=='':
        return answer
    
    tmp=divide(p)
    u=tmp[0]
    v=tmp[1]

    if check_collection(u):
        u+=final(v)
        return u
    else:
        answer+='('
        answer+=final(v)
        answer+=')'
        answer+=reverse(u)
        return answer
    return answer
    
def solution(p):
    if check_collection(p):
        return p
    
    answer=final(p)

    return answer

print(solution('()))((()'))


