def solution(n, times):
    left = 1
    right = max(times) * n   # 60분 이내로
    
    answer = 0  # 걸리는 최소 시간
    while left <= right:   # 최대 걸리는 시간보다 적을 때까지 반복
        mid = (left + right) // 2  # 중간 시점
        people = 0 # 사람
        for time in times:  # [7, 10]
            people += mid // time  # 중간 시점을 time으로 나눈다.
            # mid가 30이면 7분 걸리는 심사대에 4명이 갈 수 있음
            # 10분 걸리는 심사대에 3명이 갈 수 있음
        
        if people >= n:  # 7명이 n인 6보다 크기 때문에
            answer = mid  # mid = 30으로 설정
            right = mid - 1  # 이제 최대 시간 값은 mid-1 값이 됨
        else:  # 만약 n보다 people이 작다면
            left = mid + 1  # 왼쪽에서 1분을 더해서 구하려는 answer(mid)가 존재하는 range를 줄인다.
            # 계속 반복해서 최적의 answer 반환
            
    return answer