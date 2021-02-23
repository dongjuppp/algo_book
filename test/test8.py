import heapq
def dik(lt,distance,k):
    q=[]
    heapq.heappush(q,(0,1))
    distance[1]=0
    while q:
        dist,now=heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in range(len(lt[now])):
            cost=dist+lt[now][i][1]

            if cost<distance[lt[now][i][0]]:
                distance[lt[now][i][0]]=cost
                heapq.heappush(q,(cost,lt[now][i][0]))
    count=0
    for i in range(len(distance)):
        if distance[i]<=k:
            count+=1
    return count

def solution(N, road, K): # N노드수 road 121-> 1과2 가 1의 벨류로 양방향 연걸, k이하 길
    answer = 0
    lt=[[] for i in range(N+1)]
    distance=[int(1e9) for i in range(N+1)]
    for i in range(len(road)):
        lt[road[i][0]].append([road[i][1],road[i][2]])
        lt[road[i][1]].append([road[i][0],road[i][2]])
    
    answer=dik(lt,distance,K)

    return answer


print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))