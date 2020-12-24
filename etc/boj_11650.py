# 백준 11650 좌표정렬

num=int(input())

positions=[]

for i in range(num):
    positions.append(list(map(int,input().split( ))))

positions.sort(key=lambda x:(x[0],x[1]))

for position in positions:
    print(str(position[0])+' '+str(position[1]))