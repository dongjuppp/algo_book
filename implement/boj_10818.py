num = int(input())

lt = list(map(int, input().split(' ')))

lt = sorted(lt)

print(str(lt[0])+' '+str(lt[num-1]))