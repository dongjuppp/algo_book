from collections import deque
def solution(answers):
    answer = []
    one=deque([1,2,3,4,5])
    two=deque([ 2, 1, 2, 3, 2, 4, 2, 5])
    three=deque([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    result_1=0
    result_2=0
    result_3=0
    for num in answers:
        a=one.popleft()
        b=two.popleft()
        c=three.popleft()

        if a==num:
            result_1+=1
        if b==num:
            result_2+=1
        if c==num:
            result_3+=1
        one.append(a)
        two.append(b)
        three.append(c)
    
    if result_1>result_2 and result_1>result_3:
        answer.append(1)
    elif result_2>result_1 and result_2>result_3:
        answer.append(2)
    elif result_3>result_1 and result_3>result_2:
        answer.append(3)
    elif result_1==result_2 and result_1>result_3:
        answer.append(1)
        answer.append(2)
    elif result_1==result_3 and result_1>result_2:
        answer.append(1)
        answer.append(3)
    elif result_2==result_3 and result_2>result_1:
        answer.append(2)
        answer.append(3)
    else:
        answer.append(1)
        answer.append(2)
        answer.append(3)


    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
