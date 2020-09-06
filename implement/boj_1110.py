# 백준 1110번 더하기 사이클
num = int(input())
tmp=num
result=0

l=0
r=0

while True:
    if tmp<10:
        r=tmp
    else:
        l=tmp//10
        r=tmp%10
    plus=l+r
    tmp=plus%10+r*10
    #print(tmp)
    result+=1
    if tmp==num:
        break
    l=0
    r=0

print(result)
