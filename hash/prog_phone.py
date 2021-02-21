def solution(phone_book):
    answer = True
    phone_book.sort()
    
    dic={}
    for phone in phone_book:
        for i in range(1,len(phone)):
            if hash(phone[0:i]) in dic:
                answer=False
                break
        dic[hash(phone)]=phone
    return answer


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))


