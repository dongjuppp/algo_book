# 찢을 숫자
x = int(input())

# 코인
coins = list(map(int,input().split( )))

# 혹시나 정렬이 안되어있을 경우 정렬
coins.sort(reverse=True)

# 본체
count=0
curser=0
while(x!=0):
    if x-coins[curser]>=0:
        x=x-coins[curser]
        count+=1
    else:
        curser+=1
    
print(count)