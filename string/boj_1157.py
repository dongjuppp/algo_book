lt = list(input().upper())
result=''
alphabet=[0 for i in range(123)] # 97 ~ 122

# a 97 gap 32 A65 z122

big_position=0
big=0

for i in range(len(lt)):
    tmp=ord(lt[i])
    alphabet[ord(lt[i])]+=1
    if big<alphabet[ord(lt[i])]:
        big=alphabet[ord(lt[i])]
        big_position=ord(lt[i])

count=0
for i in range(65,123,1):
    if alphabet[i] == big:
        result=chr(i)
        count+=1

if count>1:
    print('?')
else:
    print(result)




