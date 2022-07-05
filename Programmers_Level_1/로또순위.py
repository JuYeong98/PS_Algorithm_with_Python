def solution(lottos, win_nums):
    rank_dict = {'6':1 , '5':2, '4':3 ,'3':4, '2':5}
    answer = []
    point = 0
    for lotto in lottos:
        if lotto in win_nums:
            point+=1
    zero_C = lottos.count(0)
    top_p = point+ zero_C
    if top_p <2:
        answer.append(6)
    else:
        answer.append(rank_dict[str(top_p)])
    if point <2:
        answer.append(6)
    else:
        answer.append(rank_dict[str(point)])
    return answer

def solution(lottos, win_nums):
    zero = lottos.count(0)
    a= [x for x in lottos if x in win_nums]
    max = zero+len(a)
    min = len(a)

    max = 7- max if max >=1 else 6
    min = 7- min if min >=1 else 6
    return [max,min]    