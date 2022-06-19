def solution(arr1, arr2):
    answer = [[]]
    row = len(arr1)
    col = len(arr1[0])
    for r in range(row):
        for c in range(col):
            answer[r].append(arr1[r][c] + arr2[r][c])
    return answer
    