def solution(left, right):
    answer = 0
    def num_of(n):
        count =0
        for i in range(1,n+1):
            if n%i ==0:
                count+=1
        return count
    for i in range(left, right+1):
        if num_of(i) % 2 ==0:
            answer+=i
        else:
            answer-=i
    return answer