# 프로그래머스 인형 뽑기

def solution(board, moves):
    answer = 0
    length=len(board)
    q=[0]
    idx=0
    for i in range(len(moves)):
        now=moves[i]

        doll=0
        for j in range((length)):
            if board[j][now-1]!=0:
                doll=board[j][now-1]
                board[j][now-1]=0
                break
        if doll!=0:
            if q[idx]==doll:
                answer+=2
                del q[idx]
                idx-=1
            else:
                q.append(doll)
                idx+=1


    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))
