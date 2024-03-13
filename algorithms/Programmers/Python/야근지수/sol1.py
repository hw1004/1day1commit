# https://school.programmers.co.kr/learn/courses/30/lessons/12927

def solution(n, works):
    import heapq
    
    # 먼저, n이 works의 각 요소의 합보다 크거나 같을 때 항상 result는 0이 된다.
    if n >= sum(works):
        return 0
    
    # 가장 큰 값부터 선택해서 작업을 해야 한다.
    # 따라서 최대힙을 사용하기 위해 음수형태의 힙으로 works를 변환한다.
    works = [-work for work in works]
    heapq.heapify(works)
    
    # n번의 for loop을 돌려서 음수로 변환하였기 때문에 가장 작은 값(양수로는 가장 큰 값)을 heappop한다.
    # pop으로 해당 값을 heap에서 제거하고 1을 더해서 work로 저장하였기 떄문에 다시 works에 변한 값을 포함시켜야 한다.
    for _ in range(n):
        work = heapq.heappop(works) + 1
        heapq.heappush(works, work)
    
    result = sum([work**2 for work in works])
    return result