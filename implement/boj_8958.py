# 백준 8958 ox퀴즈

num = int(input())

lines=[input() for i in range(num)]
answer=0
for line in lines:
    start=0
    for j in range(len(line)):
        if line[j]=='O':
            start+=1
            answer+=start
        else:
            start=0
    print(answer)
    answer=0
