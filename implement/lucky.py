# 책 321 럭키 스트레이트

lt=list(map(int,input()))

left=sum(lt[:len(lt)//2])
right=sum(lt[len(lt)//2:])

if left==right:
    print('LUCKY')
else:
    print('READY')