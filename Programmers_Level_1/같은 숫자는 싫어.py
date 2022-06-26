
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

def solution(arr):

    result = []
    
    for i in range(len(arr)):
        if i == 0:
            result.append(arr[i])
        # 맨 처음 숫자는 무조건 result 리스트에 담아준다.
        elif arr[i] != arr[i-1] :

            result.append(arr[i])
        
        
    return result    