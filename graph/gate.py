gate=int(input())
plane=int(input())

lt=[]

gate_in=[i for i in range(gate+1)]
count=0
sign=0
for i in range(plane):
    tmp=int(input())
    lt.append(tmp)

    for j in range(tmp,len(gate_in)):
        gate_in[j]-=1
        if gate_in[j]<0:
            sign=1
    if sign==0:
        count+=1
print(count)




