from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0])
    curr_weight = 0
    queue = deque(truck_weights)
    print(queue)
    print()
    while bridge or queue:
        if answer == 0:
            a = bridge.popleft()
        if len(queue) == 0:
            if curr_weight + w > weight: #견딜 수 있는 무게 이상이면
                print(bridge)
                for i in range(len(bridge)):
                    bridge[i][1] +=1
                if bridge[0][1] == bridge_length:
                    W= bridge.popleft()
                    curr_weight-=W[0]
            else:
                print(bridge)
                for i in range(len(bridge)):
                    bridge[i][1] +=1
                if bridge[0][1] == bridge_length:
                    W= bridge.popleft()
                    curr_weight-=W[0]
        else:
            w=queue[0]
            if curr_weight + w > weight: #견딜 수 있는 무게 이상이면
                print(bridge)
                for i in range(len(bridge)):
                    bridge[i][1] +=1
                if bridge[0][1] == bridge_length:
                    W= bridge.popleft()
                    curr_weight-=W[0]
            else:
                w = queue.popleft()
                curr_weight+=w
                bridge.append([w, 0])
                print(bridge)
                for i in range(len(bridge)):
                    bridge[i][1] +=1
                if bridge[0][1] == bridge_length:
                    W= bridge.popleft()
                    curr_weight-=W[0]
        answer+=1            
    
    print('answer : ' + str(answer))
    return answer+1
solution(2, 10, 	[7,4,5,6])    