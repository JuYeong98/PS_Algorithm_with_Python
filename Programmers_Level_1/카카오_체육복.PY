def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer

def solution(n, lost, reserve):
    reserve_set = set(reserve)-set(lost) 
    lost_set = set(lost)-set(reserve) 

    for reserve_person in reserve_set: 
        if reserve_person-1 in lost_set: 
            lost_set.remove(reserve_person-1) 
        elif reserve_person+1 in lost_set: 
            lost_set.remove(reserve_person+1) 

    return n-len(lost_set)