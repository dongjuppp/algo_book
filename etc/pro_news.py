# 프로그래머스 뉴스
import math


def solution(str1, str2):
    answer = 0
    gop=65536
    alphabet=['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    str1=str1.upper()
    str2=str2.upper()

    str1_lt=[]
    str2_lt=[]
    
    for i in range(1,len(str1)):
        if str1[i-1] in alphabet and str1[i] in alphabet:
            str1_lt.append(str1[i-1]+str1[i])
            
    for i in range(1,len(str2)):
        if str2[i-1] in alphabet and str2[i] in alphabet:
            str2_lt.append(str2[i-1]+str2[i])

    
    hap=set(str1_lt)|set(str2_lt)
    gyo=set(str1_lt)&set(str2_lt)

    if len(hap)==0:
        return gop

    l=sum([max(str1_lt.count(number),str2_lt.count(number)) for number in hap])
    r=sum([min(str1_lt.count(number),str2_lt.count(number)) for number in gyo])

    
    answer=math.floor((r/l)*gop)
    
    return answer
    

print(int(solution('FRANCE','french')))