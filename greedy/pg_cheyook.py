n = int(input())
lost = list(map(int,input().split( )))
reserve = list(map(int,input().split( )))


def solution(n, lost, reserve):
    answer = 0
    total = [1 for _ in range(n)]

    for i in reserve:
        total[i-1]=2

    for i in lost:
        total[i-1]-=1
    
    for i in range(len(total)):
        if i==0 and total[i]==2:
            if total[1]==0:
                total[0]=1
                total[1]=1
            else:
                total[0]=1
        elif i==len(total)-1 and total[i]==2:
            if total[i-1]==0:
                total[i]=1
                total[i-1]=1
            else:
                total[i]=1
        elif total[i]==2:
            if total[i-1]==0:
                total[i]=1
                total[i-1]=1
            elif total[i+1]==0:
                total[i]=1
                total[i+1]=1
            else:
                total[i]=1
    answer = sum(total)
    

    return answer


print(solution(n,lost,reserve))
