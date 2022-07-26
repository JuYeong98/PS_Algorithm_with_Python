def solution(brown, yellow):
    import math
    answer = []
    total = brown + yellow
    if math.sqrt(total) == int(math.sqrt(total)):
        return [math.sqrt(total),math.sqrt(total)]
    y_list =[]
    for i in range(1,int(yellow/2)+1):
        if yellow % i ==0:
            r=yellow/i
            if r>i and (r+2)*(i+2)==total:
                return [r+2,i+2]


    print(y_list)        
    return answer