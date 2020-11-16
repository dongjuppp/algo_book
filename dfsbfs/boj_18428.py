# 백준 18428 감시 피하기
from itertools import combinations

num=int(input())

world=[]

for i in range(num):
    world.append(list(map(str,input().split(' '))))

blanks=[]
teachers=[]
for i in range(num):
    for j in range(num):
        if world[i][j]=='X':
            blanks.append([i,j])
        if world[i][j]=='T':
            teachers.append([i,j])

blanks=list(combinations(blanks,3))

def check_detect(wall):
    
    for teacher in teachers:
        row=teacher[0]
        col=teacher[1]

        for i in range(row,num):
            if world[i][col]=='S':
                return False
            if [i,col] in wall:
                break
        for i in range(row,-1,-1):
            if world[i][col]=='S':
                return False
            if [i,col] in wall:
                break
        for i in range(col,num):
            if world[row][i]=='S':
                return False
            if [row,i] in wall:
                break
        for i in range(col,-1,-1):
            if world[row][i]=='S':
                return False
            if [row,i] in wall:
                break
    return True

result=0
for blank in blanks:
    if check_detect(blank):
        print('YES')
        result=1
        break

if result==0:
    print('NO')
