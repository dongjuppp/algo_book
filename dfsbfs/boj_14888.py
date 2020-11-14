# 백준 14888 연산자 끼워 넣기

many=int(input())

numbers=list(map(int,input().split()))

compute=list(map(int,input().split()))# + - * //

big=int(-1e10)
small=int(1e10)
count=0
def recur(num,index,com):
    global big,small,count
    lt=[0,0,0,0]
    if index==many:
        if num>big:
            big=num
        if num<small:
            small=num
    else:
        if com[0]>0:
            tmp_com=com[:]
            tmp_com[0]-=1
            count+=1
            recur(num+numbers[index],index+1,tmp_com)
        if com[1]>0:
            tmp_com=com[:]
            tmp_com[1]-=1
            recur(num-numbers[index],index+1,tmp_com)
        if com[2]>0:
            tmp_com=com[:]
            tmp_com[2]-=1
            recur(num*numbers[index],index+1,tmp_com)
        if com[3]>0:
            tmp_com=com[:]
            tmp_com[3]-=1
            recur(int(num/numbers[index]),index+1,tmp_com)
            

recur(numbers[0],1,compute)

print(big)
print(small)


