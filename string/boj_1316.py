num = int(input())


count = 0
for i in range(num):
    lt = list(input())
    prev='lt[0]'
    alpha_dic={}
    #abcabc
    for j in range(0,len(lt)):
        if prev != lt[j]:
            if lt[j] in alpha_dic:
                break
            else:
                alpha_dic[prev]=0
        prev=lt[j]
        if j == len(lt)-1:
            count+=1


print(count)
