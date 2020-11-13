# 백준 18352 특정 거리의 도시 찾기
from collections import deque
city_num,road_num,k,start=map(int,input().split())

world=[[] for i in range(city_num+1)]
visited=[False for i in range(city_num+1)]
for i in range(road_num):
    a,b=map(int,input().split())
    world[a].append(b)

def bfs():
    result=[]
    queue=deque()
    count=0
    queue.append([start,count])
    
    while queue:
        tmp=queue.popleft()
        
        if tmp[1]==k:
            result.append(tmp[0])
        for city in world[tmp[0]]:
            if not visited[city]:
                queue.append([city,tmp[1]+1])
                visited[city]=True
    return result

result=bfs()

if len(result)==0:
    print(-1)
else:
    result.sort()
    for city in result:
        print(city)
    