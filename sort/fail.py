# 책 361 실패율

def solution(N, stages):
    answer = []
    tmp_anser=[]
    numbers=[0 for i in range(N+2)]
    stages.sort()
    for i in stages:
        numbers[i]+=1
    total=sum(numbers)
    for i in range(1,N+1):
        if total==0:
            tmp=0
        else:
            tmp=numbers[i]/total
        tmp_anser.append([i,tmp])
        total-=numbers[i]
    tmp_anser.sort(key=lambda x:-x[1])
    
    for i in range(len(tmp_anser)):
        answer.append(tmp_anser[i][0])
    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))