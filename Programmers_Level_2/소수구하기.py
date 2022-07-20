from itertools import permutations
import math
def solution(numbers):
    def is_prime_num(n):
        for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
            if n % i == 0:
                return False

        return True
    num_len = len(numbers)
    answer = 0
    num_list = list(numbers)
    print(num_list)
    possible_set = set()
    for i in range(1, num_len+1):
        sub_list = list(permutations(num_list, i))
        for sub in sub_list:
            num = int(''.join(s for s in sub))
            possible_set.add(num)
        #answer+= len(sub_list)
    possible_list = list(possible_set)
    for possible in possible_list:
        if is_prime_num(possible) and possible>1:
            answer+=1
            print(possible)
    return answer