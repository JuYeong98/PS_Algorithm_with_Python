def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge  = [0 for i in range(bridge_length)]
    #print(bridge)
    while bridge:
        answer+=1
        
        bridge.pop(0)
        
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                w = truck_weights.pop(0)
                bridge.append(w)
            else:
                bridge.append(0)
        #print(bridge)        
    return answer