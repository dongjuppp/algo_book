x = int(input())
x = 1000-x
coins = [500,100,50,10,5,1]

count=0
curser=0
while(x!=0):
    if x-coins[curser]>=0:
        x=x-coins[curser]
        count+=1
    else:
        curser+=1
    
print(count)