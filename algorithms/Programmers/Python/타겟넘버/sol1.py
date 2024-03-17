# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# idx를 재귀함수로 넘겨서 더한 값과 뺀값을 반복해서 더하도록 한다.
# global을 이용해서 더한 값을 유지한다.
counts = 0
def BFS(numbers, target, current, idx):  # current는 +,- 조정해서 값들을 합한 총합
    global counts
    # 다 더한 값이 target과 같을 때 counts에 추가
    if idx == len(numbers):
        if current == target:
            counts += 1
        return  # target과 다른 값일 때 아무것도 반환하지 않는다.
    # +한 값과 -한 값
    BFS(numbers, target, current + numbers[idx], idx+1)
    BFS(numbers, target, current - numbers[idx], idx+1)
    
def solution(numbers, target):
    BFS(numbers, target, 0, 0)
        
    return counts