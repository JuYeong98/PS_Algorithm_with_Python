def solution(numbers):
    answer = []
    l = list(combinations(numbers, 2))

    for i in l:
        answer.append(i[0]+i[1])
    answer = list(set(answer))
    answer.sort()

    return answer

    from itertools import combinations

def solution(numbers):
    answer = []
    
    for i in combinations(numbers, 2):
        answer.append(i[0]+i[1])
        
    answer = list(set(answer))    
    answer.sort()
    return answer