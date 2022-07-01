def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    for d_ in d:
        total +=d_
        if total <=budget:
            answer+=1
        else:
            return answer
    return answer