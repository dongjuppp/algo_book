# 책 312 곱하기 혹은 더하기

lt=list(map(int,input()))


start=1

for num in lt:
    if num==0:
        start+=num
    else:
        start*=num

print(start)
