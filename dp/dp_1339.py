# 백준 1339 단어 수학
from itertools import permutations
n=int(input())

words=[]
chars=[]
result=0
for _ in range(n):
    tmp=(list(map(str,input())))
    words.append(tmp)
    for i in range(len(tmp)):
        if not tmp[i] in chars:
            chars.append(tmp[i])

numbers=[9-i for i in range(len(chars))]
print(numbers)
print(chars)
combi=list(permutations(numbers,len(numbers)))

for i in range(len(combi)):
    now=combi[i] 
    tmp_dict={}
    
    for j in range(len(now)):
        tmp_dict[chars[j]]=now[j]
    
    tmp_sum=[]
    for j in range(len(words)):
        tmp_result=0
        now_word=words[j]
        tw=''
        for k in range(len(now_word)):
            tw+=(str(tmp_dict[now_word[k]]))
        tmp_result+=int(tw)
        tmp_sum.append(tmp_result)
    if sum(tmp_sum)>result:
        result=sum(tmp_sum)
        

print(result)



