def solution(n,a,b):
    answer = 0
    while True:
        if a/2 == a//2:
            a = a/2
        else:
            a = a//2 +1
        if b/2 == b//2:
            b = b/2
        else:
            b = b//2 +1
        answer+=1    
        if a==b:
            break
    return answer