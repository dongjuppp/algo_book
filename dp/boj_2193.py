# 백준 2193 이친수

num=int(input())

one=[0]*91
zero=[0]*91

one[1]=1
one[3]=1
zero[2]=1
zero[3]=1

for i in range(4,num+1):
    one[i]=zero[i-1]
    zero[i]=one[i-1]+zero[i-1]

print(one[num]+zero[num])