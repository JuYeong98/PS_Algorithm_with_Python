def solution(arr):
    answer = []
    min_num = min(arr)
    for num in arr:
        if num != min_num:
            answer.append(num)
    
    return [-1] if answer ==[] else answer

"""
def rm_small(mylist):
    mylist.remove(min(mylist))
    return mylist
"""