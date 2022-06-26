def solution(s):
    answer = ''
    l = len(s)
    if l %2==0:
        h = l//2
        answer = s[h-1:h+1]
    else:
        h = l//2
        answer = s[h]
    return answer