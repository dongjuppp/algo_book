
name = input()

answer=0
name_lt=[i for i in name]
name_lt_ord=[]

for i in name_lt:
    name_lt_ord.append(min(abs(ord(i)-65),abs(90-ord(i))+1))

now=0
while(sum(name_lt_ord)!=0):
    answer+=name_lt_ord[now]
    name_lt_ord[now]=0
    for i in range((len(name_lt_ord)//2)+1):
        if now+i<len(name_lt_ord) and name_lt_ord[now+i]!=0:
            now=now+i
            answer+=i
            break
        elif (now-i)>-len(name_lt_ord) and name_lt_ord[now-i]!=0:
            now=now-i
            answer+=i
            break
    
print(answer)