#책 115페이지

n = input()

x = ord(n[0])
y = int(n[1])

x_list=[i+ord('a') for i in range(8) ]
y_list=[1,2,3,4,5,6,7,8]

#오위, 오아, 왼위, 왼아, 위오, 위왼, 아오, 아왼
x_move=[2,2,-2,-2,1,-1,1,-1]
y_move=[1,-1,1,-1,2,2,-2,-2]

count=0

for i in range(len(x_move)):
    tmp_x=x+x_move[i]
    tmp_y=y+y_move[i]

    if tmp_x in x_list and tmp_y in y_list:
        count+=1

print(count)

