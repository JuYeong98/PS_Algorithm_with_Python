def solution(progresses, speeds):
    answer = []
    to_take = []
    strikes_l =[]
    for i in range(len(progresses)):
        take = (100-progresses[i]) / speeds[i]
        if take != int(take):
            take = int(take) +1
        to_take.append(take)
    max_val = -100
    print(to_take)
    strikes = 0
    for take in to_take:
        if take > max_val:
            strikes+=1
            max_val = take
        strikes_l.append(strikes)
    max_strike = max(strikes_l)
    for i in range(1,max_strike+1):
        answer.append(int(strikes_l.count(i)))

    return answer