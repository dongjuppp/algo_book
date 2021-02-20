def solution(brown, yellow):
    answer = []
    # a*b=yello -> (a+2)*(b+2) == brown+yellow
    total_size=brown+yellow

    for i in range(1,int(yellow**0.5)+1):
        if yellow%i==0:
            if (i+2)*((yellow//i)+2)==total_size:
                answer=[(yellow//i)+2,i+2]
                break
    
    return answer

print(solution(24,24))
print(solution(10,2))
print(solution(8,1))