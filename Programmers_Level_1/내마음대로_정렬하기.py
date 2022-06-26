"""
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])

def strange_sort(strings, n):
    def sortkey(x):
        return x[n]
    strings.sort(key=sortkey)
    return strings    
"""

import numpy as np

def solution(strings, n):
    answer = []
    n_=[]
    sol = []
    for string in strings:
        n_.append(string[n])
    for i in range(len(strings)):
        sol.append((n_[i],strings[i]))
    sol = sorted(sol)
    print(sol)
    for i in range(len(strings)):
        answer.append(sol[i][1])
    return answer