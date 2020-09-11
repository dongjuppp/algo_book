# 책 149 음료수 얼려 먹기

n,m = map(int,input().split( ))

lt =[]

for i in range(n):
    tmp = list(map(int,input()))
    for j in tmp:
        lt.append(j)

visited=[False]*(n*m)

graph=[]

for i in range(len(lt)):
    tmp=[]
    if lt[i]==0:
        if i-5>=0 and lt[i-5]==0: #상
            tmp.append(i-5)
        if i+5<n*m and lt[i+5]==0: #하
            tmp.append(i+5)
        if i%m!=0 and lt[i-1]==0: #좌
            tmp.append(i-1)
        if (i+1)%m!=0 and lt[i+1]==0: #우
            tmp.append(i+1)
    graph.append(tmp)

def dfs(g,start,v):
    v[start]=True

    for i in graph[start]:
        if not visited[i]:
            dfs(g,i,v)

result=0
print(graph)
for i in range(len(lt)):
    if lt[i]==0 and visited[i]==False:
        result+=1
        dfs(graph,i,visited)

print(result)
    
    

