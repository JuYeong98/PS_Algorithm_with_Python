def solution(ls):
    return min(len(ls)/2, len(set(ls)))


def solution(nums):
    leng = len(nums) //2
    comb =list(set(nums))
    comb_len = len(comb)
    return comb_len if comb_len <=leng else leng    