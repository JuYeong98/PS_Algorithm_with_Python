def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
            
    return answer

def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer

    
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))    