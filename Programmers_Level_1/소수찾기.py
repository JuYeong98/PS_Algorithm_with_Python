def solution(n):
    cnt = [True]*(n+1)
    print(int(n**0.5)+1)
    c = 0
    for i in range(2, int(n**0.5)+1):
        if cnt[i]==True: # 만약 소수면
            for j in range(i+i, n+1, i):
                print(j)
                cnt[j] = False # 소수의 배수는 소수가 아님
    for i in range(2, n+1): # 소수 개수 카운트
        if cnt[i]:
            c+=1
    return c
solution(100)    