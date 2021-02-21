from itertools import combinations
def solution(clothes):
    answer = 1
    dic={}
    lt=[]
    for clothe in clothes:
        if clothe[1] in dic:
            dic[clothe[1]].append(clothe[0])
        else:
            dic[clothe[1]]=[clothe[0]]
    
    for key in dic.keys():
        answer*=(len(dic[key])+1)
    
    answer-=1
    return answer



print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
print(solution([["crow_mask", "face"]]))