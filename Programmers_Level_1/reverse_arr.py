

def digit_reverse(n):
    return list(map(int, reversed(str(n))))


def solution(n):
    answer = []
    while(n>=1):
        answer.append(n%10)
        n//=10

    return answer