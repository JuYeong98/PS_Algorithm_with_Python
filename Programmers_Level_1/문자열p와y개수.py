def solution(s):
    answer = True
    #p = s.count('p')+s.count('P')
    #y= s.count('y') + s.count('Y')
    if (s.count('p')+s.count('P')) == (s.count('y') + s.count('Y')):
        answer = True
    else:
        answer = False
    
    return answer