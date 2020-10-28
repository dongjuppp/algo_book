# 책 313 문자열 뒤집기

lt=input()


zero=0
one=0

if lt[0]=='0':
    one+=1
else:
    zero+=1

now='0'
for i in range(len(lt)):
    if lt[i]=='0' and now=='1':
        zero+=1
        now='0'
    elif lt[i]=='1' and now=='0':
        one+=1
        now='1'


print(min(zero,one))