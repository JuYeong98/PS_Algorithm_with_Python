def solution(n):
    answer = 0
    
    for i in range(1,n//2+1):
        sub_sum = 0
        sub_i = i
        while sub_sum<15:
            print(sub_i, end=' ')
            sub_sum +=sub_i
            sub_i +=1
            if sub_sum == n:
                answer+=1
                print()
                print(i)
        print()            
    return answer+1
solution(14)