"""
def nextSquare(n):
    from math import sqrt
    return 'no' if sqrt(n) % 1 else (sqrt(n)+1)**2
"""
import math
def solution(n):
    answer=math.sqrt(n)
    flag = 0
    if answer ==int(answer):
        flag = 1
        
    return (answer+1)*(answer+1) if flag ==1 else -1