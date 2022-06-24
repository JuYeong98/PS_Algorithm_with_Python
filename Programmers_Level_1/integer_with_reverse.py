"""
def solution(n):
    ls = list(srt(n))
    ls.sort(reverse = True)
    return int("", join(ls))
"""
def solution(n):
    answer = ''
    n  = str(n)
    str_list = []
    for i in range(len(n)):
        str_list.append(n[i])
    str_list.sort(reverse = True)
    for i in range(len(n)):
        answer+=str_list[i]
    answer = int(answer)    
    return answer