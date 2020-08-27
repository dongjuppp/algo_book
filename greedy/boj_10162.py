t = int(input())

lt=[300,60,10]

five=0
one=0
ten=0

if t%10>=1:
    print(-1)
else:
    if t>=300:
        a=int(t/300)
        t=(t-(300*a))
        five=a
    if t>=60:
        a=int(t/60)
        t=(t-(60*a))
        one=a
    if t>=10:
        a=int(t/10)
        t=(t-(10*a))
        ten=a
    print(five, one, ten)
