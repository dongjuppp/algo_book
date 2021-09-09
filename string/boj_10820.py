

# a97 122
# 0 47 57
# A 65 90

while True:
    s=0
    b=0
    d=0
    g=0
    try:
        lt = list(input())
        for i in range(len(lt)):
            now = ord(lt[i])

            if 97 <= now <=122:
                s+=1
            if 65<= now <= 90:
                b+=1
            if 47<= now <= 57:
                d+=1
            if lt[i]==' ':
                g+=1
        print(str(s)+' '+str(b)+' '+str(d)+' '+str(g))
    except EOFError:
        break
