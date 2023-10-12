N = int(input())
answer = []
for i in range(N):
    word = list(input().split(' '))
    answer.append([])
    for w in word:
        w = w[::-1]
        
        answer[i].append(w+' ')
        
for a in answer:
    print(''.join(a))