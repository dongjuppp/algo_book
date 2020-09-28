# 백준 2805 나무 자르기

tree_num,cut=map(int,input().split())

trees=list(map(int,input().split( )))

end=max(trees)
start=0
result=0


while(start<=end):
    mid=(start+end)//2

    tmp=0
    for i in range(len(trees)):
        if mid<trees[i]:
            tmp+=trees[i]-mid
        
    if tmp<cut:
        end=mid-1
    else:
        result=mid
        start=mid+1

print(result)