N = int(input())
cow = {}
answer = 0
for i in range(N):
    cow_num , pos = map(int, input().split())
    if cow_num in cow:
        if cow[cow_num] != pos:
            cow[cow_num] = pos
            answer+=1
    else:
        cow[cow_num] = pos
print(answer)