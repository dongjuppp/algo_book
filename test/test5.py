def solution(participant, completion):
    answer = ''
    ha={}
    
    for person in completion:
        ha[person]=1
    print(ha)
    for person in participant:
        if not person in ha:
            answer=person
            break
        else:
            if participant.count(person)==2:
                answer=person
                break
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))