def solution(n):
    answer = 0
    base_3 = ''
    while n>=1:
        l = n%3
        base_3+=str(l)
        n//=3
    print(base_3)    
    for i in range(len(base_3)):
        n = len(base_3) -i-1
        answer+= pow(3,i) * int(base_3[n]) 
    return answer


def solution(n):
    answer = 0
    base_3 = ''
    while n>=1:
        l = n%3
        base_3+=str(l)
        n//=3
    print(base_3)    
    for i in range(len(base_3)):
        n = len(base_3) -i-1
        answer+= pow(3,i) * int(base_3[n]) 
    return answer