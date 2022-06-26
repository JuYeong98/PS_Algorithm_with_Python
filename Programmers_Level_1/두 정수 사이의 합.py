"""
def adder(a, b):
    # 함수를 완성하세요
    if a > b: a, b = b, a

    return sum(range(a,b+1))
"""


def solution(a, b):
    big  = a if a >b else b
    small  = a if a<b else b
    answer = 0
    for i in range(small,big+1):
        answer+=i
    return answer