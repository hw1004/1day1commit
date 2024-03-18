# https://school.programmers.co.kr/learn/courses/30/lessons/42628

def solution(operations):
    import heapq
    answer = []
    
    heapq.heapify(answer)
    for i in operations:
        if i[:2] == "I ":
            heapq.heappush(answer, int(i[2:]))
        if i == 'D 1':
            try:
            # 최댓값을 삭제하기 위해서는 음수로 변형해준 후 heappop을 하고 거기서 원래 양수값 반환
                max_heap = []
                heapq.heapify(max_heap)
                for k in answer:
                    heapq.heappush(max_heap, (-k, k))
                max_item = heapq.heappop(max_heap)[1]
                answer = []
                heapq.heapify(answer)
                for k in max_heap:
                    heapq.heappush(answer, k[1])
            except:
                continue
        if i == 'D -1':
            try:
                heapq.heappop(answer)
            except:
                continue
    if answer == []:
        return [0,0]
    else:
        max_heap = []
        heapq.heapify(max_heap)
        for p in answer:
            heapq.heappush(max_heap,(-p,p))
        return [heapq.heappop(max_heap)[1], heapq.heappop(answer)]
    
solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])