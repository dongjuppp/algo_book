# 백준 19533 길이 문자열 실패

n=int(input())

def compute(target):
    result=''
    t_len = len(str(target))+1
    next=target-1
    lt=[]
    # 100일때
    while True:
        lt.append(str(target))
        t_len=len(str(target))+1 # t_len=4
        target=target-t_len # 96

        if target==1:
            lt.append("1")
            break
        if target==0:
            break
    return lt

    
    

tmp_result=[]
for i in range(n):
    a,b=map(int,input().split( ))
    target=a*(10**b)
    result=compute(target)
    tmp_result.append(result)

for string in tmp_result:
    string.reverse()
    if string[0]=='2':
        s=('-'+'-'.join(string))
        if len(s)>=21:
            for i in range(17):
                print(s[i],end='')
            print('...')
        else:
            print(s)
    else:
        s=('-'.join(string))
        if len(s)>=21:
            for i in range(17):
                print(s[i],end='')
            print('...')
        else:
            print(s)
        