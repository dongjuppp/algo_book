lt = list(input())

lt.sort(reverse=True)

if lt[-1] != '0':
    print('-1')
else:
    num = 0

    for i  in range(len(lt)):
        num += int(lt[i])
    
    if num % 3 == 0:
        total = ''.join(lt)
        print(total)
    else:
        print('-1')