litsen= set()
look= set()

l, r = list(map(int, input().split(' ')))


for i in range(l):
    litsen.add(input())

for i in range(r):
    look.add(input())

gyo = litsen & look

lt = list(gyo)

lt.sort()

print(len(lt))
for i in range(len(lt)):
    print(lt[i])