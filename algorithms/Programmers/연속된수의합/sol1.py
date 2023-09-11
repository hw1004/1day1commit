# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    answer = []
    
    for i in range(-1000, 1000):
        start = i
        summ = 0
        for j in range(num):
            summ += start + j
        if summ == total:
            for k in range(num):
                answer.append(start+k)
            
    return answer

print(solution(3, 12)) # [3, 4, 5]
print(solution(5, 15)) # [1, 2, 3, 4, 5]
print(solution(4, 14)) # [2, 3, 4, 5]
print(solution(5, 5)) # [-1, 0, 1, 2, 3]