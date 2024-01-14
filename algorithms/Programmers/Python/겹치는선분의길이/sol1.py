# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    answer = 0
    # -100 ~ 100까지 count (0부터 200 인덱스를 위해 보정)
    count = [0 for i in range(200)]
    for line in lines:
        for i in range(line[0], line[1]): 
            count[i + 100] += 1
    # 점이 겹치는 개수
    answer += count.count(2) 
    answer += count.count(3) 
    return answer


print(solution([[0, 1], [2, 5], [3, 9]]))   # 2
print(solution([[-1, 1], [1, 3], [3, 9]]))   # 0
print(solution([[0, 5], [3, 9], [1, 10]]))   # 8

