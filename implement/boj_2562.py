#백준 2562 최대값

lt=[int(input()) for i in range(9)]

print(max(lt))
print(lt.index(max(lt))+1)