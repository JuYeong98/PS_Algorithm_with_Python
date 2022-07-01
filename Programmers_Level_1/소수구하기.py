def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer

from itertools import combinations
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True 
def solution(nums):
    answer = 0
    n_list = list(combinations(nums,3))
    #print(n_list)
    s_list = []
    for l in n_list:
        s_list.append(l[0]+l[1]+l[2])

    #s_list = list(set(s_list))
    for s in s_list: 
        if(is_prime(s)):
            answer+=1
    return answer