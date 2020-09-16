# 백준 4963 섬의 개수
result=[]
w=0
h=0
#상 하 좌 우 좌상 좌하 우상 우하
w_move=[0,0,-1,1,-1,-1,1,1]
h_move=[-1,1,0,0,-1,1,-1,1]

def dfs(start_w,start_h,visited):
    global w,h
    visited[start_h][start_w]=True
    
    load=[]
    
    for i in range(8):
        tmp_w=start_w+w_move[i]
        tmp_h=start_h+h_move[i]
        if tmp_w<0 or tmp_w>=w or tmp_h<0 or tmp_h>=h:
            continue
        if graph[tmp_h][tmp_w]==1:
            load.append([tmp_h,tmp_w])
    
    for ld in load:
        if not visited[ld[0]][ld[1]]:
            dfs(ld[1],ld[0],visited)

while True:
    graph=[]
    connect=[]
    visited=[]
    w,h=map(int,input().split( ))
    if w==0 and h==0:
        break
    for i in range(h):
        tmp=list(map(int,input().split( )))
        visited.append([False]*w)
        graph.append(tmp)
    re=0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==False:
                re+=1
                dfs(j,i,visited)
    result.append(re)


for i in range(len(result)):
    print(result[i])