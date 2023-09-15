T = int(input())

for tc in range(1, T+1):
    N = int(input())
        
    # 모든 요소가 1인 N X N matrix 생성
    lists = []
    for _ in range(N):
        line = []
        for _ in range(N):
            line.append(1)
        lists.append(line)
    
    ci = [0, 0]    # current index
    
    i = 1    # matrix에 채워질 수
    
    # index의 row와 column에 더해져야 할 값의 규칙
    for j in range(N-1, 0, -1):
        # 규칙에서 첫번째 row에 한하여 더해지는 값
        if j == N-1:
            while ci[1] < N-1:
                lists[int(ci[0])][int(ci[1])] = i
                ci[1] += 1
                i += 1
        # N이 홀수일 때의 규칙
        if N % 2:
            for _ in range(1, j+1):
                lists[ci[0]][ci[1]] = i
                ci[0] += (-1) ** j
                i += 1
            for _ in range(1, j+1):
                lists[ci[0]][ci[1]] = i
                ci[1] += (-1) ** (j+1)
                i += 1
        # N이 짝수일 때의 규칙
        if N % 2 == 0:
            for _ in range(1, j+1):
                lists[ci[0]][ci[1]] = i
                ci[0] += (-1) ** (j+1)
                i += 1
            for _ in range(1, j+1):
                lists[ci[0]][ci[1]] = i
                ci[1] += (-1) ** j
                i += 1
        # 달팽이숫자에서 마지막으로 오는 숫자(N ** 2)
        if i == N ** 2:
            lists[ci[0]][ci[1]] = i
    
    
    print(f'#{tc}')        
    for line in lists:
        line = [str(i) for i in line]
        print(' '.join(line))
            
            
            

        
            
            
        