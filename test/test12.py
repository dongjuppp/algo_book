def solution(n):
    answer = 0

    if n<10:
        return n
    
    start=10
    idx=9
    while True:
        st=str(start)
        #idx+=len(st)
        if idx+len(st)>=n:
            lt=list(map(str,st))
            answer=int(lt[n-idx-1])
            break
        start+=1
        idx+=len(st)


    return answer

print(solution(15))