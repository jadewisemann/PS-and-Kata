from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0 

    while bridge:
        time += 1 
        current_weight -= bridge.popleft()
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)
    return time
