# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 10:00 ~ 10:45
# 큐 자료구조를 사용하여 해결(list)
# sum을 사용하면 시간초과가 일어났다.

def solution(bridge_length, weight, truck_weights):
    # 주어진 길이의 bridge를 list로 만들자
    bridge = [0] * bridge_length
    time = 0
    sum_weight = 0 # sum을 사용하면 시간초과
    # 1초가 지날 때마다 bridge에서 하나씩 빠진다. leftpop
    # 그리고 트럭을 또 들여보낼지 아닐지 정한다.
    while len(truck_weights) != 0:
        time += 1
        sum_weight -= bridge.pop(0) # 시간 경과
        
        # sum함수를 사용하면 시간초과 일어남!!
        if sum_weight + truck_weights[0] <= weight:
            i = truck_weights.pop(0)
            bridge.append(i)
            sum_weight += i
        else:
            bridge.append(0) # 시간은 경과하기 때문에 무게의 이유로 다음 트럭이 대기해야 하면 0을 넣어준다.
            
    # len(truck_weights)가 0이 되었다는 것은 마지막 대기 트럭이 bridge를 건너고 있다는 뜻이다.
    # 따라서 bridge_length만큼 더해준다.
    time += bridge_length

    return time
        
        
            
        
            
        
        
            
            
    return answer