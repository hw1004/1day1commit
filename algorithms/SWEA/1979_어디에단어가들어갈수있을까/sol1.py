T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    
    matrix = []
    
    for i in range(N):
        matrix.append(list(map(int, input().split())))
        
    total = 0
    
    # row에서 연속된 1이 k번 나오는 경우 탐색
    for row in matrix:
        for i in range(1, N-K):
            if row[i:i+K] == [1] * K and row[i-1] == 0 and row[i+K] == 0:
                total += 1
        if row[0:K] == [1] * K and row[K] == 0:
            total += 1
        if row[N-K:] == [1] * K and row[N-K-1] == 0:
            total += 1
            
    
    # column에서 연속된 1이 K번 나오는 경우 탐색
    columns = []
    column = []
    for i in range(N):
        for j in range(N):
            column.append(matrix[j][i])
        columns.append(column)
        column = []
    
    for col in columns:
        for i in range(1, N-K):
            if col[i:i+K] == [1] * K and col[i-1] == 0 and col[i+K] == 0:
                total += 1
        if col[0:K] == [1] * K and col[K] == 0:
            total += 1
        if col[N-K:] == [1] * K and col[N-K-1] == 0:
            total += 1
                
    print(f'#{tc} {total}')
        
        