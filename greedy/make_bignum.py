#프로그래머스 큰 수 만들기
def solution(number, k):
    answer=''
    big=0
    length=len(number)-k
    minus=0
    answer_list=[]
    start=0
    big_index=0
    while True:
        count=0
        for i in range(start,start+k+1):
            if int(number[i])>big:
                big_index=i
                minus=k-count
                big=int(number[i])
            count+=1
        answer_list.append(number[big_index])
        k=minus
        start=big_index+1
        big=0
        if k==0:
            break
    

    return answer.join(answer_list)+number[start:]