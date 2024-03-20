# https://school.programmers.co.kr/learn/courses/30/lessons/43238

# 17:12 ~ 17:54

def solution(n, times):
    # [7, 10]이라고 하면 7, 14, 21, 28..분을 기준으로 첫번째 심사대가 비고
    # 10, 20, 30...분을 기준으로 두번째 심사대가 빈다.
    # 이 두개를 합쳐 7, 10, 14, 20, 21, 28, 30으로 심사대가 비는 타임라인을 생성하면
    # 6번째 사람이 심사를 받는 것이 끝나는 28분이 return 값이 된다.
    timeline = []
    for time in times:
        for i in range(1, n):
            timeline.append(time*i)
            
    # timeline을 오름차순으로 정렬
    timeline = sorted(timeline)
    return timeline[n-1]

print(solution(6,[7,10]))