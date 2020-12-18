# 최종 순위 책 399

test_case=int(input())

def compute():
    teams=int(input())
    ex_year=list(map(int,input().split( )))
    change_num=int(input())
    lt=[]
    for i in range(change_num):
        lt.append(list(map(int,input().split( ))))
    