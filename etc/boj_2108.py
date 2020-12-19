# 백준 2108 통계학
import sys
import operator
n=int(input())
lt=[]
my_dict={}
for i in range(n):
    num=int(sys.stdin.readline().rstrip())
    lt.append(num)
    if not num in my_dict:
        my_dict[num]=1
    else:
        my_dict[num]+=1
s_dict=sorted(my_dict.items(),key= lambda x:(x[1],-x[0]))
#print(my_dict)
#print(s_dict)

avg=round(sum(lt)/len(lt))

lt.sort()
mid=lt[len(lt)//2]
num_range=lt[-1]-lt[0]

ex=0
if len(s_dict)>1:
    ex=s_dict[-1][0]
    if s_dict[-1][1]==s_dict[-2][1]:
        ex=s_dict[-2][0]
else:
    ex=s_dict[0][0]


print(avg)
print(mid)
print(ex)
print(num_range)