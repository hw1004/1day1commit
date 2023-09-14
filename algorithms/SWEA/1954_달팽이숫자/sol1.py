T = int(input())

for tc in range(1, T+1):
    N = int(input())
        
    lists = []
    for _ in range(N):
        line = []
        for _ in range(N):
            line.append(1)
        lists.append(line)
    
    ci = [0, 0]    # current index
    
    i = 1
    
    for j in range(N-1, 0, -1):
        if j == N-1:
            while ci[1] < N-1:
                lists[int(ci[0])][int(ci[1])] = i
                ci[1] += 1
                i += 1
        if N % 2:
            for _ in range(1, j+1):
                lists[ci[0]][ci[1]] = i
                ci[0] += (-1) ** j
                i += 1
            for _ in range(1, j+1):
                lists[ci[0]][ci[1]] = i
                ci[1] += (-1) ** (j+1)
                i += 1
        if N % 2 == 0:
            for _ in range(1, j+1):
                lists[ci[0]][ci[1]] = i
                ci[0] += (-1) ** (j+1)
                i += 1
            for _ in range(1, j+1):
                lists[ci[0]][ci[1]] = i
                ci[1] += (-1) ** j
                i += 1
        if i == N ** 2:
            lists[ci[0]][ci[1]] = i
    
    
    print(f'#{tc}')        
    for line in lists:
        line = [str(i) for i in line]
        print(' '.join(line))
            
            
            

        
            
            
        