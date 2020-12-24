#백준 1181 단어 정렬

num=int(input())
lt=[]

for i in range(num):
    lt.append(input())

tmp=set(lt)
lt=list(tmp)
lt.sort(key=lambda x: (len(x),x))

for word in lt:
    print(word)