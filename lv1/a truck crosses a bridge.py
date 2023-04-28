# 실행시간 초과(case 5)
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [0 for _ in range(bridge_length)]
#     print("(변수)bridge = ", bridge)
#     while bridge:
#         answer += 1
#         print("1. answer = ", answer)
#         bridge.pop(0)
#         print("2. bridge.pop = ", bridge)
#
#         if truck_weights:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 t = truck_weights.pop(0)
#                 print("3. t = ", t)
#                 bridge.append(t)
#                 print("4. (if)bridge(t) = ", bridge)
#             else:
#                 bridge.append(0)
#                 print("5. (else)bridge(0) = ", bridge)
#
#     return answer
#

# 실행시간은 통과되지만 case 5번 9900ms 나옴...
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     bridge = [0] * bridge_length
#     while len(bridge):
#         answer += 1
#         print("1. answer = ", answer)
#         bridge.pop(0)
#         print("2. bridge(pop) = ", bridge)
#         if truck_weights:
#             if sum(bridge) + truck_weights[0] <= weight:
#                 print("3. bridge, truck_weights[0] = ", bridge, truck_weights[0])
#                 bridge.append(truck_weights.pop(0))
#                 print("4. bridge(append) = ", bridge)
#             else:
#                 bridge.append(0)
#                 print("5. (else)bridge = ", bridge)
#     return answer

from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    tot_weight = 0
    step = 0
    sorted(truck_weights, reversed=True)
    print("1. (reverse)truck_weights = ", truck_weights)

    while rtw:
        print("2. (-bridge.pop)tot_weight = ", tot_weight)
        tot_weight -= bridge.popleft()
        if tot_weight + truck_weights[-1] > weight:
            bridge.append(0)
            print("3. (if)bridge.append(0) = ", bridge)
        else:
            truck = truck_weights.pop()
            print("4. (else)truck_weight.pop() = ", truck)
            bridge.append(truck)
            print("5. (else)bridge.append(truck) = ", bridge)
            tot_weight += truck
            print("6. (else)tot_weight += truck = ", tot_weight)
        step += 1
        print("7. step += 1 = ", step)
    step += bridge_length
    return step

bridge_length = 2
weight = 10
truck_weights = [5, 6, 3, 2, 4, 9, 4]
#truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))

