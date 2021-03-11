def solution(A):
    A.sort()
    start=1
    for i in range(len(A)):
        if A[i]>start:
            break
        elif A[i]==start:
            start+=1
    return start

print(solution([1, 3, 6, 4, 1, 2]))