# 책 329 기둥과 보 설치

def check_pillar_create(x,y,world):
    if x==0:
        return True
    if world[y][x]==2 or world[y-1][x]==1 or world[y][x-1]==2:
        return True
    return False

def check_pillar_delete(x,y,world):
    # 기둥삭제시 문제 => 위에 기둥이 있을경우, 위의 보가 다른기둥과 없을때
    if (world[y+1][x]==1 and world[y+1][x-1]!=2):
        return False
    if (world[y+1][x]==1 and world[y+1][x]!=2):
        return False
    
    if (world[y+1][x]==2 and world[y][x+1]!=1):
        if not (world[y+1][x-1]==2 and world[y+1][x+1]==2):
            return False
    if world[y+1][x-1]==2 and world[y][x-1]!=1:
        if not (world[y+1][x]==2 and world[y+1][x-2]==2):
            return False
    return True

def check_wall_create(x,y,world):
    if world[y-1][x]==1:
        return True
    if world[y-1][x+1]==1:
        return True
    if world[y][x-1]==2 and world[y][x+1]==2:
        return True
    return False

def check_wall_delelte(x,y,world):
    # 보 삭제시 문제=> 위에가 기둥, 양옆의 보가 자신이 필요한경우
    if (world[y][x]==1):
        if world[y][x-1]!=1:
            return False
    if (world[y][x+1]==2 and (world[y-1][x+1]!=1 and world[y-1][x+2]!=1)):
        return False
    if (world[y][x-1]==2 and (world[y-1][x-1]!=1 and world[y-1][x-2]!=1)):
        return False
    return True

#x,y 0기1보 0삭1설
#world 0없음 1기둥 2보 3겹쳐
def solution(n, build_frame):
    answer = []
    world=[]

    for i in range(n+1):
        tmp=[]
        for j in range(n+1):
            tmp.append(0)
        world.append(tmp)
    
    leng=len(build_frame)

    for build in build_frame:
        x,y,typ,how=map(int,build)
        tmp=[x,y]
    return answer


test1=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(5,test1))