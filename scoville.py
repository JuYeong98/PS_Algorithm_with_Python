import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    heapq.heapify(scoville)
    #print(scoville)
        
    while True:
        if scoville[0] <K:
            if len(scoville) < 2:
                return -1
            input1 = heapq.heappop(scoville)
            input2 = heapq.heappop(scoville)
            new_member = input1 + (2* input2)
            heapq.heappush(scoville , new_member)
            answer+=1
        else:
            break
    return answer