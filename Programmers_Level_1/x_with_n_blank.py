def solution(x, n):
    answer = []
    sum = x
    origin = x
    for i in range(n):
        answer.append(sum)
        sum +=origin
    return answer

