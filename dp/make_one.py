# 책 217페이지 1로 만들기

num=int(input())

memo={}

def foo(tmp,count):
    if tmp==1:
        return count
    
    lt=[]
    
    if tmp%5==0:
        lt.append(foo(tmp//5,count+1))
    if tmp%3==0:
        lt.append(foo(tmp//3,count+1))
    if tmp%2==0:
        lt.append(foo(tmp//2,count+1))

    lt.append(foo(tmp-1,count+1))


    return min(lt)

print(foo(num,0))
