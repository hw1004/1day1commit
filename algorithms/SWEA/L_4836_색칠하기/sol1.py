T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    
    colors = []
    for _ in range(N):
        point = [int(i) for i in input().split()]
        colors.append(point)
    
    # 10 x 10 행렬
    matrix = [[0] * 10 for _ in range(10)]
    
    for color in colors:
        for row in range(color[0], color[2]+1):
            for column in range(color[1], color[3]+1):
                # 0일 경우 color[4]로 채워 넣음
                if matrix[row][column] == 0:
                    matrix[row][column] = color[4]
                # 1일 경우, 그리고 color[4]이 2일 경우 3으로 바꿈
                if matrix[row][column] == 1 and color[4] == 2:
                    matrix[row][column] = 3
                # 2일 경우, 그리고 color[4]이 1일 경우 3으로 바꿈
                if matrix[row][column] == 2 and color[4] == 1:
                    matrix[row][column] = 3
    
    duplicate = 0
    for row in matrix:
        for element in row:
            if element == 3:
                duplicate += 1
                

    print(f'#{testcase} {duplicate}')
            