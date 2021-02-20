from itertools import permutations
def isPrimary(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
        if count>=3:
            return False
    if count==2:
        return True
    else:
        return False


def solution(numbers):
    answer = 0
    lt=[i for i in list(map(str,numbers))]
    
    nums=[]
    total_number=[]
    
    for i in range(1,len(lt)+1):
        nums.append(list(permutations(lt,i)))
    
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            tmp=''
            for k in range(len(nums[i][j])):
                tmp+=nums[i][j][k]
            total_number.append(int(tmp))
    
    result_list=list(set(total_number))
    for i in range(len(result_list)):
        if isPrimary(result_list[i]):
            answer+=1
    return answer

print(solution('17'))