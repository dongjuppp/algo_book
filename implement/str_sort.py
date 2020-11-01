# 책 322 문자열 재정렬

print(ord('0')) #48-57
string=list(map(str,input()))

string.sort()

num=0
s=''
for tmp in string:
    if ord(tmp)>=48 and ord(tmp)<=57:
        num+=int(tmp)
    else:
        s+=tmp

s+=str(num)
print(s)
