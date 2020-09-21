# 백준 11656 접미사

string = input()

lt=[]

for i in range(len(string)):
    lt.append(string[i:])

lt.sort()


for i in range(len(lt)):
    print(lt[i])