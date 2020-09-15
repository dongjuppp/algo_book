# 백준 11724 연결요소

n,m=map(int,input().split( ))

graph=[[] for i in range(n+1)]
visited=[False for i in range(n+1)]

result=0

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a) 
    

def dfs(start):
    if visited[start]:
        return
    visited[start]=True

    for i in graph[start]:
        dfs(i)


for j in range(1,n+1):
    if not visited[j]:
        result+=1
        dfs(j)
    
print(result)