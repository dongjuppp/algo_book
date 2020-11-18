# 백준 1715 카드 정렬하기
import heapq
num=int(input())

q=[]
for i in range(num):
    heapq.heappush(q,int(input()))

result=0
while len(q)!=1:
    one=heapq.heappop(q)
    two=heapq.heappop(q)

    tmp=one+two
    result+=tmp
    heapq.heappush(q,tmp)

print(result)
