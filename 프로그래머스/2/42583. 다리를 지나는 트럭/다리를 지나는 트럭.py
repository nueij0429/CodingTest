from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length) #다리 길이만큼 채워서 다리를 만듦
    total_weight = 0
    truck_weights = deque(truck_weights) # 대기 중인 트럭들

    while bridge:
        time += 1
        exited = bridge.popleft()
        total_weight -= exited
        
        if truck_weights:
            if (total_weight + truck_weights[0]) <= weight:
                truck = truck_weights.popleft()
                
                bridge.append(truck)
                
                total_weight += truck
            else:
                bridge.append(0)
                
    return time
                
    