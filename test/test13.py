def solution(s):
    answer = 0
    
    lt=list(map(str,s))
    
    for i in range(len(lt)):
        if lt[i]=='a':
            for j in range(i+1,len(lt)):
                if lt[j]=='a':
                    break
                if lt[j]=='z':
                    answer+=1
                    break
        if lt[i]=='z':
            for j in range(i+1,len(lt)):
                if lt[j]=='z':
                    break
                if lt[j]=='a':
                    answer+=1
                    break
    return answer

print(solution("zabzczxa"))
print(solution("abcd"))
print(solution("abcz"))