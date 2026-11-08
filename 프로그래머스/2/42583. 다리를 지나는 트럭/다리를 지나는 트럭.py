from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    answer = 0
    truck_weights = deque(truck_weights)
    sum_weight = 0
    while truck_weights:
        answer += 1
        sum_weight -= bridge.popleft()
        
        if sum_weight + truck_weights[0] <= weight:
            cur = truck_weights.popleft()
            bridge.append(cur)
            sum_weight += cur
        else:
            bridge.append(0)
    return answer + bridge_length