n,m = map(int,input().split(' '))

lt = []

for _ in range(n):
    lt.append(list(map(int,input().split(' '))))


# x,y
line = [
    [[0,0],[1,0],[2,0],[3,0]],
    [[0,0],[0,1],[0,2],[0,3]],
    [[0,0],[-1,0],[-2,0],[-3,0]],
    [[0,0],[0,-1],[0,-2],[0,-3]]
]

squre = [
    [[0,0],[1,0],[1,-1],[0,-1]],
    [[0,0],[0,-1],[-1,-1],[-1,0]],
    [[0,0],[0,1],[1,1],[1,0]],
    [[0,0],[0,1],[-1,1],[-1,0]]
]

nieun = [
    [[0,0],[0,1],[0,2],[1,0]],
    [[0,0],[1,0],[2,0],[0,-1]],
    [[0,0],[-1,0],[0,-1],[0,-2]],
    [[0,0],[-1,0],[-2,0],[0,1]]
]

sunder = [
    [[0,0],[0,1],[1,0],[1,-1]],
    [[0,0],[-1,0],[0,1],[1,1]],
    [[0,0],[-1,0],[-1,1],[0,-1]],
    [[0,0],[0,-1],[-1,-1],[1,0]]
]

fuck = [
    [[0,0],[1,0],[-1,0],[0,-1]],
    [[0,0],[0,-1],[0,1],[1,0]],
    [[0,0],[1,0],[-1,0],[0,1]],
    [[0,0],[0,-1],[0,1],[-1,0]]
]

def go_line(x,y):
    result = 0
    
    for i in range(4):
        now = line[i]
        
        tmp = 0
        # tmp_x = x
        # tmp_y = y
        for j in range(4):
            tmp_x = x + now[j][0]
            tmp_y = y+ now[j][1]
            
            if tmp_x<0 or tmp_x>=m or tmp_y<0 or tmp_y>=n:
                break
            tmp += lt[tmp_y][tmp_x]
        result = max(result, tmp)
    return result

def go_squre(x,y):
    result = 0
    for i in range(4):
        now = squre[i]
        
        tmp = 0
        
        for j in range(4):
            tmp_x = x+ now[j][0]
            tmp_y = y+ now[j][1]
            
            if tmp_x<0 or tmp_x>=m or tmp_y<0 or tmp_y>=n:
                break
            tmp += lt[tmp_y][tmp_x]
        result = max(result, tmp)
    return result

def go_nieun(x,y):
    result = 0
    
    if x==2 and y==2:
        print()
    for i in range(4):
        now = nieun[i]
        
        tmp = 0
        
        for j in range(4):
            tmp_x = x+ now[j][0]
            tmp_y = y+ now[j][1]
            
            if tmp_x<0 or tmp_x>=m or tmp_y<0 or tmp_y>=n:
                break
            tmp += lt[tmp_y][tmp_x]
        result = max(result, tmp)
    return result

def go_sunder(x,y):
    result = 0
    for i in range(4):
        now = sunder[i]
        
        tmp = 0
      
        for j in range(4):
            tmp_x = x + now[j][0]
            tmp_y = y + now[j][1]
            
            if tmp_x<0 or tmp_x>=m or tmp_y<0 or tmp_y>=n:
                break
            tmp += lt[tmp_y][tmp_x]
        result = max(result, tmp)
    return result

def go_fuck(x,y):
    result = 0
    for i in range(4):
        now = fuck[i]
        
        tmp = 0
       
        for j in range(4):
            tmp_x = x+  now[j][0]
            tmp_y = y+now[j][1]
            
            if tmp_x<0 or tmp_x>=m or tmp_y<0 or tmp_y>=n:
                break
            tmp += lt[tmp_y][tmp_x]
        result = max(result, tmp)
    return result


result = 0
for i in range(n):
    for j in range(m):
        
        l = go_line(j, i)
        s = go_squre(j, i)
        e = go_nieun(j, i)
        t = go_sunder(j, i)
        f = go_fuck(j, i)
        
        tmp = max(l, s, e, t, f)
        
        result = max(result, tmp)

print(result)
        
                
            