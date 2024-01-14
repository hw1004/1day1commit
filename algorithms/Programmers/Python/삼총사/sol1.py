# https://school.programmers.co.kr/learn/courses/30/lessons/131705 

def solution(number):
    
    combi = 0
    
    for f in range(len(number)-2):
        for s in range(f+1, len(number)-1):
            for t in range(s+1, len(number)):
                if number[f] + number[s] + number[t] == 0:
                    combi += 1
    return combi


print(solution([-2, 3, 0, 2, -5]))  # 2
print(solution([-3, -2, -1, 0, 1, 2, 3]))  # 5
print(solution([-1, 1, -1, 1]))  # 0